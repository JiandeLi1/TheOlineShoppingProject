import mysql.connector
from mysql.connector import errorcode

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
        return "can not connect DB."
    cursor = mydb.cursor(buffered=True)

    # can ignore the id parameter if there already has one row in table.
    sql = f"INSERT INTO users (email, password, username) VALUES ('{email}','{password}','{username}')"

    try:
        cursor.execute(sql)
        mydb.commit()
        cursor.close()
        mydb.close()
        return "add user succussful."
    except mysql.connector.Error as err:
        print(str(err))
        return str(err)