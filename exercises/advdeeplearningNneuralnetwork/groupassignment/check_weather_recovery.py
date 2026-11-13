#!/usr/bin/env python3
"""Check missing weather cells against FMI without changing the input CSV.

Requires Python 3.10+, pandas and numpy. Networking uses Python's standard library.

Preview (no requests):
  python check_weather_recovery.py dataset_mansion.csv
Check the known shared outage:
  python check_weather_recovery.py dataset_mansion.csv --fetch --start 2021-07-18 --end 2021-07-19
Check all dates (potentially many requests):
  python check_weather_recovery.py dataset_mansion.csv --fetch
Optionally write a SEPARATE candidate dataset, for review:
  python check_weather_recovery.py dataset_mansion.csv --fetch --write-candidate

Each run creates a new timestamped output folder. Responses are cached separately
and reused unless --refresh is set. An empty successful response is not cached.
Cached data reflects its download time; it is not a promise of current coverage.
FMI manual: https://en.ilmatieteenlaitos.fi/open-data-manual-time-series-data
This uses the same hourly observation query and station as create_house_dataset.py.
"""

import argparse
import hashlib
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd

ENDPOINT = 'https://opendata.fmi.fi/wfs'
QUERY = 'fmi::observations::weather::hourly::multipointcoverage'
STATION = '101339'
FIELDS = {
    'ta_pt1h_avg': 'AirTemperature(degC)',
    'ta_pt1h_max': 'HighestTemperature(degC)',
    'ta_pt1h_min': 'LowestTemperature(degC)',
    'rh_pt1h_avg': 'RelativeHumidity(%)',
    'ws_pt1h_avg': 'WindSpeed(m/s)',
    'ws_pt1h_max': 'MaximumWindSpeed(m/s)',
    'ws_pt1h_min': 'MinimumWindSpeed(m/s)',
    'wd_pt1h_avg': 'WindDirection(deg)',
    'pra_pt1h_acc': 'PrecipitationAmount(mm)',
    'pri_pt1h_max': 'MaximumPrecipitationIntensity(mm/h)',
    'pa_pt1h_avg': 'AirPressure(hPa)',
    'wawa_pt1h_rank': 'PresentWeather(rank)',
}
WEATHER = list(FIELDS.values())
METADATA = ['Latitude', 'Longitude', 'Place']
NS = {
    'gmlcov': 'http://www.opengis.net/gmlcov/1.0',
    'gml': 'http://www.opengis.net/gml/3.2',
    'swe': 'http://www.opengis.net/swe/2.0',
}

def local_name(tag):
    return tag.rsplit('}', 1)[-1]

def parse_response(xml):
    """Read named XML fields; never assume the weather parameter order.

    The source script's multipoint format uses latitude, longitude, epoch seconds
    for each position. Unexpected shape, duplicates or XML errors are rejected.
    """
    root = ET.fromstring(xml)
    errors = [e.text.strip() for e in root.iter()
              if local_name(e.tag) in {'ExceptionText', 'ServiceException'} and e.text]
    if errors:
        raise ValueError('FMI exception: ' + '; '.join(errors))
    if local_name(root.tag) != 'FeatureCollection':
        raise ValueError('Expected an FMI FeatureCollection, not this response type.')

    # Check station identifiers when the response provides them.
    stations = {e.text.strip() for e in root.iter()
                if e.text and any(str(v).rstrip('/').endswith('/fmisid')
                                  for v in e.attrib.values())}
    if stations and stations != {STATION}:
        raise ValueError(f'Unexpected station identifiers: {stations}')

    places = {}
    for point in root.findall('.//gml:Point', NS):
        pos = point.find('gml:pos', NS)
        name = point.find('gml:name', NS)
        if pos is not None and pos.text and name is not None and name.text:
            coords = pos.text.split()
            if len(coords) == 2:
                places[tuple(map(float, coords))] = name.text.strip()

    rows = []
    coverages = root.findall('.//gmlcov:MultiPointCoverage', NS)
    if not coverages:
        # A valid FeatureCollection with no observation members is a successful
        # query with no records, not a recoverable measurement.
        if any(local_name(e.tag) == 'member' and len(e) for e in root.iter()):
            raise ValueError('Nonempty response uses an unsupported observation format.')
        return pd.DataFrame(columns=WEATHER + METADATA,
                            index=pd.DatetimeIndex([], tz='UTC', name='MTime'))
    for coverage in coverages:
        fields = coverage.findall('.//swe:DataRecord/swe:field', NS)
        names = [e.attrib.get('name', '').lower() for e in fields]
        if not names or len(set(names)) != len(names):
            raise ValueError('Missing or duplicate parameter names in XML.')
        if not any(name in FIELDS for name in names):
            raise ValueError(f'No recognized hourly parameters: {names}')
        positions = coverage.find('.//gmlcov:positions', NS)
        tuples = coverage.find('.//gml:doubleOrNilReasonTupleList', NS)
        if positions is None or tuples is None:
            raise ValueError('Missing positions or weather tuple list.')
        pos_tokens = (positions.text or '').split()
        value_tokens = (tuples.text or '').split()
        if len(pos_tokens) % 3 or len(value_tokens) != len(pos_tokens) // 3 * len(names):
            raise ValueError('Position/measurement lengths do not match.')
        for i in range(len(pos_tokens) // 3):
            lat, lon, epoch = map(float, pos_tokens[i * 3:i * 3 + 3])
            if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                raise ValueError('Unexpected coordinate order or invalid position.')
            timestamp = pd.to_datetime(epoch, unit='s', utc=True)
            if timestamp != timestamp.floor('h'):
                raise ValueError('Source returned an off-hour timestamp.')
            values = value_tokens[i * len(names):(i + 1) * len(names)]
            row = {'MTime': timestamp}
            for name, token in zip(names, values):
                if name in FIELDS:
                    # Missing tokens stay missing. Unexpected text fails loudly.
                    value = float(token) if token.lower() not in {'nil', 'missing', 'nodata'} else np.nan
                    row[FIELDS[name]] = value if math.isfinite(value) else np.nan
            # Recover metadata only from a returned hourly position with at least
            # one real weather measurement, not by forward-filling a constant.
            if any(pd.notna(row.get(c)) for c in WEATHER):
                row.update({'Latitude': lat, 'Longitude': lon,
                            'Place': places.get((lat, lon), pd.NA)})
            rows.append(row)
    if not rows:
        return pd.DataFrame(columns=WEATHER + METADATA,
                            index=pd.DatetimeIndex([], tz='UTC', name='MTime'))
    frame = pd.DataFrame(rows).set_index('MTime').sort_index()
    if frame.index.has_duplicates:
        raise ValueError('Source response has duplicate hourly timestamps.')
    return frame.reindex(columns=WEATHER + METADATA)

def request_url(day):
    return ENDPOINT + '?' + urlencode({
        'service': 'WFS', 'version': '2.0.0', 'request': 'GetFeature',
        'storedquery_id': QUERY, 'fmisid': STATION,
        'starttime': day.strftime('%Y-%m-%dT00:00:00Z'),
        'endtime': day.strftime('%Y-%m-%dT23:59:59Z'),
    })

def fetch_day(day, cache, refresh=False, attempts=3, timeout=30):
    cache_file = cache / f'{STATION}_{day:%Y-%m-%d}.xml'
    url = request_url(day)
    if cache_file.exists() and not refresh:
        content = cache_file.read_bytes()
        try:
            return parse_response(content), url, 'cache'
        except (ValueError, ET.ParseError):
            # Re-query a broken or incompatible cached response.
            pass
    for attempt in range(attempts):
        try:
            req = Request(url, headers={'User-Agent': 'HouseWeatherRecoveryCheck/1.0'})
            with urlopen(req, timeout=timeout) as response:
                content = response.read()
            frame = parse_response(content)
            if not frame.empty:
                temp = cache_file.with_suffix('.xml.tmp')
                temp.write_bytes(content)
                temp.replace(cache_file)
            return frame, url, 'network'
        except HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt == attempts - 1:
                raise
        except (URLError, TimeoutError, OSError):
            if attempt == attempts - 1:
                raise
        # Exponential delay, capped; no retry for an invalid XML payload.
        time.sleep(min(2 ** (attempt + 1), 10))
    raise RuntimeError('Request attempts exhausted.')

def audit_missing(frame, columns, fetched, day_status, selected_rows):
    """One report row per ORIGINAL missing cell in the selected time window."""
    rows = []
    for timestamp in frame.index[selected_rows]:
        day = timestamp.floor('D')
        for column in columns:
            if pd.notna(frame.at[timestamp, column]):
                continue
            status = day_status.get(day, 'not_queried')
            value = pd.NA
            if status == 'success':
                if timestamp not in fetched.index:
                    status = 'no_source_record'
                else:
                    value = fetched.at[timestamp, column]
                    status = 'recoverable' if pd.notna(value) else 'still_missing_at_source'
            rows.append({'MTime_UTC': timestamp, 'Feature': column,
                         'Status': status, 'Source value': value})
    return pd.DataFrame(rows, columns=['MTime_UTC', 'Feature', 'Status', 'Source value'])

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('input', type=Path)
    parser.add_argument('--fetch', action='store_true', help='Make requests; default is preview only.')
    parser.add_argument('--start', help='First UTC date to check, YYYY-MM-DD (inclusive).')
    parser.add_argument('--end', help='Last UTC date to check, YYYY-MM-DD (inclusive).')
    parser.add_argument('--columns', help='Comma-separated original column names; default: weather and location.')
    parser.add_argument('--max-days', type=int, help='Check only the first N affected UTC days in the selected window.')
    parser.add_argument('--output-dir', type=Path, default=Path('weather_recovery_reports'))
    parser.add_argument('--cache-dir', type=Path, default=Path('weather_recovery_cache'))
    parser.add_argument('--refresh', action='store_true', help='Download again instead of using saved responses.')
    parser.add_argument('--write-candidate', action='store_true', help='Also create a separate candidate CSV with only recoverable blanks filled.')
    args = parser.parse_args()
    if args.max_days is not None and args.max_days < 1:
        parser.error('--max-days must be at least 1.')
    if args.write_candidate and not args.fetch:
        parser.error('--write-candidate requires --fetch.')

    original_hash = hashlib.sha256(args.input.read_bytes()).hexdigest()
    raw = pd.read_csv(args.input)
    if 'MTime' not in raw:
        parser.error('Input must have an MTime column.')
    timestamps = pd.to_datetime(raw['MTime'], utc=True, errors='raise')
    if timestamps.isna().any() or timestamps.duplicated().any():
        parser.error('Resolve missing or duplicate timestamps first.')
    frame = raw.copy()
    frame.index = pd.DatetimeIndex(timestamps)
    allowed = WEATHER + METADATA
    columns = args.columns.split(',') if args.columns else [c for c in allowed if c in frame]
    columns = list(dict.fromkeys(c.strip() for c in columns))
    if not columns or any(c not in allowed or c not in frame for c in columns):
        parser.error('--columns must name existing weather/location columns, never Consumption.')
    # Validate weather numeric parsing without silently turning bad strings into NaN.
    for col in columns:
        if col != 'Place':
            pd.to_numeric(frame[col], errors='raise')
    selected = np.ones(len(frame), dtype=bool)
    if args.start:
        selected &= frame.index >= pd.to_datetime(args.start, utc=True).floor('D')
    if args.end:
        selected &= frame.index < pd.to_datetime(args.end, utc=True).floor('D') + pd.Timedelta(days=1)
    affected = frame.loc[selected, columns].isna().any(axis=1)
    affected_index = affected.index[affected]
    days = affected_index.floor('D').unique().sort_values()
    print(f'Missing selected cells: {int(frame.loc[selected, columns].isna().sum().sum()):,}')
    print(f'Affected UTC days: {len(days):,}')
    days_to_check = days[:args.max_days] if args.max_days else days
    print(f'Days planned for this run: {len(days_to_check):,}')

    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')
    run = args.output_dir / stamp
    run.mkdir(parents=True, exist_ok=False)
    plan = pd.DataFrame({'UTC date': days.strftime('%Y-%m-%d'),
                         'Selected for request': days.isin(days_to_check)})
    plan.to_csv(run / 'request_plan.csv', index=False)
    statuses, logs, downloaded = {}, [], []
    if args.fetch:
        args.cache_dir.mkdir(parents=True, exist_ok=True)
        for n, day in enumerate(days_to_check, 1):
            print(f'[{n}/{len(days_to_check)}] {day:%Y-%m-%d}', flush=True)
            try:
                data, url, origin = fetch_day(day, args.cache_dir, args.refresh)
                if not data.empty and not (data.index.floor('D') == day).all():
                    raise ValueError('Source returned records outside the requested UTC day.')
                statuses[day] = 'success'
                downloaded.append(data)
                logs.append({'UTC date': str(day.date()), 'Status': 'success',
                             'Source': origin, 'Returned hours': len(data),
                             'URL': url, 'Error': ''})
            except (HTTPError, URLError, TimeoutError, OSError, ValueError, ET.ParseError) as exc:
                statuses[day] = 'request_failed'
                logs.append({'UTC date': str(day.date()), 'Status': 'request_failed',
                             'Source': 'network_or_cache', 'Returned hours': 0,
                             'URL': request_url(day), 'Error': str(exc)})
                print(f'  Could not check this date: {exc}', flush=True)
            time.sleep(.7)  # Deliberately below FMI's documented request-rate limit.
    fetched = (pd.concat(downloaded).sort_index() if downloaded else
               pd.DataFrame(columns=allowed, index=pd.DatetimeIndex([], tz='UTC')))
    if fetched.index.has_duplicates:
        raise ValueError('Duplicate source timestamps across query days.')
    audit = audit_missing(frame, columns, fetched, statuses, selected)
    audit.to_csv(run / 'missing_cell_audit.csv', index=False)
    summary_rows = []
    for col in columns:
        part = audit[audit['Feature'] == col]
        counts = part['Status'].value_counts()
        row = {'Feature': col, 'Missing in selected window': len(part)}
        for status in ['recoverable', 'still_missing_at_source', 'no_source_record', 'request_failed', 'not_queried']:
            row[status] = int(counts.get(status, 0))
        summary_rows.append(row)
    summary = pd.DataFrame(summary_rows)
    summary.to_csv(run / 'recovery_summary.csv', index=False)
    pd.DataFrame(logs, columns=['UTC date', 'Status', 'Source', 'Returned hours', 'URL', 'Error']).to_csv(run / 'request_log.csv', index=False)
    fetched.to_csv(run / 'downloaded_weather.csv', index_label='MTime_UTC')
    metadata = {'input': str(args.input.resolve()), 'input_sha256': original_hash,
                'checked_at_UTC': stamp, 'station': STATION, 'query': QUERY,
                'fetch_enabled': args.fetch, 'columns': columns,
                'start': args.start, 'end': args.end, 'max_days': args.max_days,
                'interpretation': 'Recovered historical observations, not weather forecasts. Existing observed values are never replaced.'}
    (run / 'run_details.json').write_text(json.dumps(metadata, indent=2))
    if args.write_candidate:
        candidate = frame.copy()
        for col in columns:
            part = audit[(audit['Feature'] == col) & audit['Status'].eq('recoverable')]
            if not part.empty:
                replacements = (part['Source value'].to_numpy() if col == 'Place' else
                                pd.to_numeric(part['Source value'], errors='raise').to_numpy(dtype=float))
                candidate.loc[pd.DatetimeIndex(part['MTime_UTC']), col] = replacements
        # Existing nonmissing values, row order, timestamp strings and Consumption
        # must remain exactly as loaded. No absent timestamps are inserted.
        observed = frame.notna()
        if not candidate.where(observed).equals(frame.where(observed)):
            raise AssertionError('An existing observation changed; candidate not written.')
        candidate.to_csv(run / 'dataset_mansion_recovery_candidate.csv', index=False)
    if hashlib.sha256(args.input.read_bytes()).hexdigest() != original_hash:
        raise AssertionError('Input file changed during the run.')
    print('\n' + summary.to_string(index=False))
    print(f'\nReports: {run.resolve()}')
    if not args.fetch:
        print('Preview only: no requests made. Use --fetch to check FMI availability.')
    print('Original CSV unchanged. Recoverable does not mean independently validated.')
    return run

if __name__ == '__main__':
    main()
