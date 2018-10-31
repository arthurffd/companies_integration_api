# Data Integration Challenge
This is the Data Integration Challenge project<br />

## Purpose: 
  this document contains necessary information to run the application and explain the purposes and expecet results.<br />
<br />
Customer: Neoway <br />
Developer: Arthur Flores Duarte <br />
<br />
Created Date: 2018/10/22 <br />
Last Updates:  <br />
<br />
<br />
## Project Files:
  ####  appfull.py - Main application source code in Python
  Setup:<br />
    * Loads companies data from file (q1_catalog.csv) to a dataframe;<br />
    * Prepares and transform data;<br />
    * Creates an instance from entity Companies;<br />
              <br />
            API:<br />
                Setup API using FLASK framework package;<br />
                <br />
                Class Company (Resource):<br />
                    Methods:<br />
                        * get: HTTP GET method - search a company by name and zip code. <br />
                            Input: <br />
                                HTTP Request - GET - http://127.0.0.1:5000/company<br />
                                Name and ZipCode should be informed in JSON content, example:<br />
                                  {"company_name": "pizza hut" , "zip_code": "44667"}<br />
                                    <br />
                            Results:<br />                   
                                200: in case of the company was found, return HTTP code "200" and also the company information;<br />
                                404: if didn't find any company related, return HTTP code "404 and the message "company not found";<br />
<br />
      <br />                          
                        * put: PUT HTTP method - update a company website information.<br />
                            Input: <br />
                                HTTP Request - PUT - http://127.0.0.1:5000/company<br />
                                Name, ZipCode and Website should be informed in JSON content, example:<br />
                                  {"company_name": "tim dieball", "zip_code": "53115", "website": "http://motorsport-coatings.com" }<br />
   <br />                         
                            Results:<br />
                                200: in case of the company was found, update the company website attribute. Then return HTTP code "200" and also the updated company information;<br />
                                     <br />
                                404: if didn't find any company related, return HTTP code "404 and the message "company not found";<br />
                            
   <br />           
                Run API interface<br />
                    * URL: http://127.0.0.1:5000/company<br />
