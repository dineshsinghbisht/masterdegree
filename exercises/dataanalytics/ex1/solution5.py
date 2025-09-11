##### imports #####

import requests
import json
import sys

# this has to do with pass by value / reference
from copy import deepcopy

##### config #####

english = True
# english = False


##### helpers #####


# notebook replacement of sys.exit()
# call with raise StopExecution
class StopExecution(Exception):
    def _render_traceback_(self):
        pass

query_template = {
    "query": [], # list of query items
    "response": {
        "format": "json"
    }
}

query_item_template = {
    "code": "", # variable
    "selection": {
        "filter": "item",
        "values": [] # list of strings
    }
}


##### main #####


with requests.Session() as session:

    '''
    first, some browsing in order to get the correct database
    you can do this with a browser too (but translation may become an issue)
    '''

    lang_id = 'en' if english else 'fi'
    base_url = f'https://pxdata.stat.fi/PXWeb/api/v1/{lang_id}/StatFin'
    response = session.get(base_url)

    for item in response.json():
        print(item['id'], item['text'])

    # stop execution
    # raise StopExecution

    '''
    next, append the id of your thing of interest to the url
    (EDIT the adopt below)
    '''

    catalogue_url = f'{base_url}/rtie'
    response = session.get(catalogue_url)

    '''
    check what .px files are available in the "catalogue"
    '''
    for item in response.json():
        print(item['id'], item['text'])

    # stop execution
    # raise StopExecution

    '''
    once you decide what .px file interests you, 
    EDIT it below in order to fetch the available data headers

    '''

    headers_url = f'{base_url}/rtie/statfin_rtie_pxt_12lz.px'
    response = session.get(headers_url)

    myjson = response.json()
    print()
    print('variables:', len(myjson['variables']))
    print()
    for var in myjson['variables']:
        print(var['text'])
    print()

    if english:
        tmp_url = headers_url.replace('/en/','/fi/')
        response = session.get(tmp_url)
        myjson = response.json()
        print('the corresponding variables in finnish (may needed in the actual query):')
        print()
        for var in myjson['variables']:
            print(var['text'])
        print()

    # stop execution
    # raise StopExecution

    '''
    okay, but then things get more serious as we build the actual query for the data

    first, fetch the maximum values that one can download
    (this is kind of hi-tech, got it from the documentation)
    (which typically sucks in free & public apis like this)
    '''
    response = session.get(f'https://statfin.stat.fi/PXWeb/api/v1/{lang_id}/?config')
    maxvalues = response.json()['maxValues']

    '''
    query building (we don't request anything yet)
    please edit only the "for myvar" line
    '''
    query = deepcopy(query_template)
    total_values = 1
    for myvar in ['Vetokalustolaji', 'Vuosi', 'Tiedot']: # EDIT this line
        #Vetokalustolaji Vuosi Tiedot
        myvalues = []
        query_item = deepcopy(query_item_template)
        for v in myjson['variables']:
            if v['code'] == myvar:
                myvalues = v['values']
        total_values = total_values * len(myvalues)
        query_item['code'] = myvar
        query_item['selection']['values'] = myvalues
        query['query'].append(query_item)
    if total_values > maxvalues:
        print('your query is too big, try again with fewer variables')
        raise StopExecution


    '''
    obtain the actual data with a "post" request
    that's like submitting a web form
    and cannot be done by gui browsing anymore
    '''
    response = session.post(headers_url, json=query)

    '''
    finally, dump the data to a file
    '''
    myjson = response.json()
    with open('test.json', 'w') as handle:
        json.dump(myjson, handle, indent=4)

    print("file created")