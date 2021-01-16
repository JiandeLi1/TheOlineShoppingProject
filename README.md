# TheOlineShoppingProject

The front-End for this project, I will not use any tools or framework because the motivation for yhis project is practicing CSS and original DOM.

This is a branch that add Backend server to this project.
See if it is ok.

## How to deploy backend server?
1. Install latest python3 on your computer.
https://www.python.org/downloads/

2. Create virtual enviroment and activate it.
Because this backend is using Flask, your need to create a virtual enviroment in case to run the server.
flask link:
https://flask.palletsprojects.com/en/1.1.x/installation/#python-version
Create a project folder and a venv folder within:
```
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```
On Windows:
```
py -3 -m venv venv
```
Activate the environment
```
. venv/bin/activate
```
On Windows:
```
> venv\Scripts\activate
```

3. Install all library in requirements.txt
The requirements.txt has all library that you need to run this program, install them.
```
pip install requirements.txt 
```

4. Run the server
Mac OS:
```
python3 test.py
```
Windows:
```
py test.py
```

## When use database
Because we are using local database, you have to make sure you already install mysql database first.
And you have to change your database name and password in sqlTest.py file
```
mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",# change it if diff
            password = 'ps123456',# change it if diff
            database = "test_db",# change it if diff
            auth_plugin='mysql_native_password'
        )
```

Since id key set as AUTO_INCREMENT, that means if table is not empty, you can add entry into table without id parameter.
If table is empty, you have to insert a entry into table first, than the program will work.

## Debugging Backend APIs
A easier way to debug backend APIs is use postman, it can easier to call APIs with parameters.
tutorial:
https://www.guru99.com/postman-tutorial.html

## Update Log
date: 01-16-2021
Add basic backend function to this project.
Connect database when user to register, use mysql database.

date: 01-16-2021
Add find/update/delete functions to Backend.
