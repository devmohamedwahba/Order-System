# Order System
Application used to manage order system 
# Overview
this is a simple structure for manging orders  it consists of two types of users 
* admin user
* ordinary user
admin user can create Product , modify Product , delete Product, list all available products
  
science fixer api did not respond correct I make work around  That can git all available currency when app start running and save them to my local database 

# Requirements
* Python 3.8.5 
# Installation
- virtualenv venv
- source venv/bin/activate
- pip install -r requirements.txt
# Test
-  python manage.py test
# Run
python manage.py runserver 
# List of Api
* create two types of user 
  * http://127.0.0.1:8000/api/user/create/
* get token to authenticate to system
  * http://127.0.0.1:8000/api/user/token/

    
***** 
## these Api should have Authorization Token
* example  
    * Authorization Token 8e1145bb9037690be258aeacb64cda63134563e6

* can show and edit information of user you should be authorized
    * http://127.0.0.1:8000/api/user/me/
    
* can show and edit and delete currency 
    * http://127.0.0.1:8000/api/product/currency/
    
* can show and edit and delete Product 
    * http://127.0.0.1:8000/api/product/product/
    
* you can purchase to any product 
    * http://127.0.0.1:8000/api/product/order/
  
* get purchased product
    * http://127.0.0.1:8000/api/product/product/purchased-product/
  
* get total revenue
    * http://127.0.0.1:8000/api/product/order/total-revenue/