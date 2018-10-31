#Challenge Makefile


start:
#TODO: commands necessary to start the API
    1- Files "appfull.py" and "q1_catalog.csv" should be in the same directory;
    2- Execute the following python script to run start the API: "appfull.py" . Example: "python  appfull.py"


check:
#TODO: include command to test the code and show the results
   1 - Files "q2_clientData.csv" and "client_test.py" should be in the same directory; 
   2 - After start the API, you can test it by executing the following script: "client_test.py" Example: "python client_test.py". 
   
   GET - Retrieves company information using company_name AND zip_code:
   GET http://127.0.0.1:5000/company
   JSON Content example: {"company_name": "epic", "zip_code": "84101"}

   PUT - Update company website information
   PUT http://127.0.0.1:5000/company
   JSON Content example: {"company_name": "tim dieball", "zip_code": "53115", "website": "www.timdie.com"}

#setup:
#if needed to setup the enviroment before starting it
