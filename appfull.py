
# coding: utf-8

import pandas as pd
import os
 
# Reading companies data from file to a dataframe
dirpath = os.path.dirname(os.path.realpath(__file__))
df_co = pd.read_csv(dirpath + '\\q1_catalog.csv', delimiter=';', header=0, names=['company_name','zip_code'], dtype={'zip_code': str})
#df_co.head()

# adding columns "id" and "website" in the dataframe
df_co['id'] = df_co.index
df_co = df_co[['id', 'company_name', 'zip_code']]
df_co['website'] = 'NA'
#df_co.dtypes
#df_co.head()

# convert dataframe to a dictionary
companies = df_co.to_dict('records')
companies


##############################
# API
##############################
# Installing FLASK API framework package
#get_ipython().system('pip install flask-restful')
    
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Defining class Company and HTTP methods
class Company(Resource):

    # GET - Search for a company using name and zip_code
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('company_name')
        parser.add_argument('zip_code')
        args = parser.parse_args()
        for company in companies:
            if((company['company_name'].upper().find(args['company_name'].upper()) >= 0) & (company['zip_code'] == args['zip_code'])):
                return company, 200

        return 'Company not found', 404		

	# PUT - Update a company website
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('company_name')
        parser.add_argument('zip_code')
        parser.add_argument('website')
        args = parser.parse_args()
        
        for company in companies:
                if(company['company_name'] == args['company_name'] and company['zip_code'] == args['zip_code']):
                    company['website'] = args['website']
                    return company, 200
        
        return 'Company not found', 404


# running API
api.add_resource(Company, '/company')

app.run(debug='True')
