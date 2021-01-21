from flask import Flask, render_template, request, redirect, jsonify
import webbrowser
import json
import os
import db
import logging
import db_test

app = Flask(__name__)

# init logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logging.log',mode = 'a')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/test1',methods=['GET'])
def test1():
    print("test1 method is called.")
    db_res = db_test.test1('xiaoming','email','xiao@gmail.com')
    logger.info(json.dumps(db_res))
    print("test1 method is end.")
    return jsonify({'status' : 'finish'})

@app.route('/test2',methods=['GET'])
def test2():
    print('test2 method is called.')
    db_res = db_test.test2('xiaojun','email','wuxiaojun@gmail.com')
    logger.info(json.dumps(db_res))
    print('test2 method is end.')
    return jsonify({'status' : 'finish'})

@app.route('/test3',methods=['GET'])
def test3():
    logger.info('test3 method is called.')
    db_res = db_test.test3('xiaojun')
    logger.info(json.dumps(db_res))
    logger.info('test3 method is end.')
    return db_res

@app.route('/test4',methods=['GET'])
def test4():
    logger.info('test4 method is called.')
    db_res = db_test.test4('xiaojun')
    logger.info(json.dumps(db_res))
    logger.info('test4 method is end.')
    return db_res


@app.route("/find",methods=['GET'])
def find_user():
    try:
        username = request.args.get('username')
    except Exception as e:
        jsonify({'error' : str(e)})

    db_res = db.getUser(username)
    if 'error' in db_res:
        return db_res

    return db_res, 200

if __name__ == "__main__":
    webbrowser.open_new("localhost:8080")
    app.run("localhost", 8080, debug=True)