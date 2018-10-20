
# coding: utf-8

# In[1]:


import pandas as pd


# In[64]:


df_co = pd.read_csv('C:\\Users\\afduarte\\Desktop\\DataScience\\Neoway\\q1_catalog.csv',delimiter=';',header=0,names=['company_name','zip_code'],dtype={'zip_code': str})

df_co.head(10)


# In[65]:


df_co['id'] = df_co.index


# In[66]:


df_co.dtypes


# In[67]:


df_co = df_co[['id', 'company_name', 'zip_code']]
df_co['website'] = 'NA'


# In[68]:


df_co.head()


# In[70]:


df_co.loc[(df_co["company_name"] == 'directv') & (df_co["zip_code"] == '38006')]


# In[77]:


# convert to dictionary
companies = df_co.to_dict('records')
companies


# In[ ]:


# API
# Using FLASK api framework


# In[73]:


#get_ipython().system('pip install flask-restful')
    


# In[91]:

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

api = Api(app)


class Company(Resource):
    def get(self, name):
        for company in companies:
            if(name == company['company_name']):
                return company, 200
        return 'Company not found', 404

    def put(self, name):
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

                         

api.add_resource(Company, '/company/<string:name>')

app.run(debug='True')
