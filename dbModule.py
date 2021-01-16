import mysql.connector
from mysql.connector import errorcode
import json

def dbConnector():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = 'ps123456',
            database = "test_db",
            auth_plugin='mysql_native_password'
        )
        return mydb
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("something wrong with username or password.")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("DB dose not exist.")
        else:
            print(e)
    return None

def init():
    mydb = dbConnector()
    cursor = mydb.cursor(buffered=True)

    fileBuffer = open('create_table.sql','r')
    sqlFile = fileBuffer.read()
    fileBuffer.close()

    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except mysql.connector.Error as err:
            print(err)

def add_user(username,password,email):
    mydb = dbConnector()
    if mydb == None:
        return json.dumps({"error":"can not find DB."})
    cursor = mydb.cursor(buffered=True)

    # can ignore the id parameter if there already has one row in table.
    sql = f"INSERT INTO users (email, password, username) VALUES ('{email}','{password}','{username}')"

    try:
        cursor.execute(sql)
        mydb.commit()
        cursor.close()
        mydb.close()
        return json.dumps({"msg" : "Add user successful."})
    except mysql.connector.Error as err:
        return json.dumps({"error" : str(err)})

def find_user(column_name,data_value):
    mydb = dbConnector()
    if mydb == None:
        return None
    cursor = mydb.cursor(buffered=True)

    query = f"SELECT * FROM users WHERE {column_name} = '{data_value}'"

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        return json.dumps({'error' : str(err)})
    
    result_set = cursor.fetchall()
    json_data = [dict(zip([key[0] for key in cursor.description],row))
                for row in result_set]

    cursor.close()
    mydb.close()

    def myConverter(o):
        if isinstance(o,datetime.datetime):
            return o.__str___()

    return json.dumps({'user' : json_data} ,default = myConverter)

def update_user(username,column_name,value_name):
    mydb = dbConnector()
    if mydb == None:
        return json.dumps({'status' : "fails"}) 
    cursor = mydb.cursor(buffered=True)

    query = f"UPDATE users SET {column_name} = '{value_name}' WHERE username = '{username}'"

    try:
        cursor.execute(query)
        mydb.commit()
    except mysql.connector.Error as err:
        return json.dumps({'error' : str(err)})

    cursor.close()
    mydb.close()

    def myConverter(o):
        if isinstance(o,datetime.datetime):
            return o.__str___()

    return json.dumps({'status' : "success"},default = myConverter)

def delete_user(username):
    mydb = dbConnector()
    if mydb == None:
        return json.dumps({"status" : "fails"})
    cursor = mydb.cursor(buffered=True)

    query = f"DELETE FROM users WHERE username = '{username}'"

    try:
        cursor.execute(query)
        mydb.commit()
    except mysql.connector.Error as err:
        return json.dumps({'error' : str(err)})

    cursor.close()
    mydb.close()

    def myConverter(o):
        if isinstance(o,datetime.datetime):
            return o.__str___()

    return json.dumps({'status' : "success"},default = myConverter)
        

init()