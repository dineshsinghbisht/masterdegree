import datetime
import numpy as np
import csv

# Read entire CSV as strings to create a 2d array
data = np.genfromtxt("prob4_ah4323.csv", delimiter=",", dtype=str)
np.savetxt("output_data.csv", data, delimiter=",", fmt="%s") ## For debugging to see the output

# Remove rows containing "nan" (string form)
clean_data = data[~np.any(data == "nan", axis=1)]
np.savetxt("output_clean_data.csv", clean_data, delimiter=",", fmt="%s") ## For debugging to see the output

# Keep the header and rows separately
header, rows = clean_data[0], clean_data[1:]

# Find the index of the "time" column
time_col_idx = np.where(header == "time")[0][0]


# Convert Unix time to formatted string
for row in rows:
    try:
        ts = float(row[time_col_idx])
        dt = datetime.datetime.utcfromtimestamp(ts)   # convert to UTC datetime
        row[time_col_idx] = dt.strftime("%m/%d/%Y %H:%M:%S")
    except ValueError:
        pass  # if time value is not valid, skip


averages = []
for i, colname in enumerate(header):
    if i == time_col_idx:
        averages.append("nan")  # placeholder for time column
    else:
        col_vals = rows[:, i].astype(float)
        averages.append(f"{np.mean(col_vals):.6f}")

formatted_data_with_header_averages = np.vstack([header, rows, averages]) 

np.savetxt("output_formatted_data_averages.csv", formatted_data_with_header_averages, delimiter=",", fmt="%s") ## For debugging to see the output