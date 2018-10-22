import pandas as pd
import os

# read file with companies website
dirpath = os.path.dirname(os.path.realpath(__file__))
dfx = pd.read_csv(dirpath + '\\q2_clientData.csv', delimiter =';', header=0, names = ['company_name', 'zip_code', 'website'],  dtype={'zip_code': str})
dfx.head(5)

# HTTP Requests
import requests
url = "http://127.0.0.1:5000/company"

# Update companies website calling the API (HTTP PUT method), using data from file csv
for index, row in dfx.iterrows():
    data_json = {"company_name": row['company_name'], "zip_code": row['zip_code'], "website" : row['website']}
    r = requests.put(url, json=data_json)
    print('Update website for company: ', row['company_name'], ' - STATUS: ', r.status_code)

# Requesting companies data calling the API (HTTP GET method)
for index, row in dfx.iterrows():
    data_json = {"company_name": row['company_name'], "zip_code": row['zip_code']}
    r = requests.get(url, json=data_json)
    print('Searching company: ', row['company_name'], ' STATUS: ', r.status_code, '\n Content: \n', r.content, '\n\n')