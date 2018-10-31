# Data Integration Challenge
This is the Data Integration Challenge project

Purpose: this document contains necessary information to run the application and explain the purposes and expecet results.

Customer: Neoway
Developer: Arthur Flores Duarte

Created Date: 2018/10/22
Last Updates:
........

Project Files:
    Source codes:
        appfull.py - Main application:
            Setup:
                * Loads companies data from file (q1_catalog.csv) to a dataframe;
                * Prepares and transform data;
                * Creates an instance from entity Companies;
              
            API:
                Setup API using FLASK framework package;
                
                Class Company (Resource):
                    Methods:
                        * get: HTTP GET method - search a company by name and zip code. 
                            Input: 
                                HTTP Request - GET - http://127.0.0.1:5000/company
                                Name and ZipCode should be informed in JSON content, example:
                                  {"company_name": "pizza hut" , "zip_code": "44667"}
                                    
                            Results:                   
                                200: in case of the company was found, return HTTP code "200" and also the company information;
                                404: if didn't find any company related, return HTTP code "404 and the message "company not found";

                                
                        * put: PUT HTTP method - update a company website information.
                            Input: 
                                HTTP Request - PUT - http://127.0.0.1:5000/company
                                Name, ZipCode and Website should be informed in JSON content, example:
                                  {"company_name": "tim dieball", "zip_code": "53115", "website": "http://motorsport-coatings.com" }
                            
                            Results:
                                200: in case of the company was found, update the company website attribute. Then return HTTP code "200" and also the updated company information;
                                     
                                404: if didn't find any company related, return HTTP code "404 and the message "company not found";
                            
              
                Run API interface
                    * URL: http://127.0.0.1:5000/company
