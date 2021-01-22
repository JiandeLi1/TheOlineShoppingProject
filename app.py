from flask import Flask, render_template, request, redirect, jsonify
import webbrowser
import json
import os
import db
import logging

app = Flask(__name__, template_folder="templates", static_folder = "static")

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from data_models import User

# init logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logging.log',mode = 'w')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Showing the home page.
@app.route("/", methods=["GET"])
def redirect_home():
    logger.info('render home page')
    return render_template("index.html",name=None)

"""
------------------------- user account operation -----------------------
"""
@app.route("/register", methods=["POST", "GET"])
def register():
    logger.info('render register page.')
    if request.method == "POST":
        res = request.form
        email = res["email"]
        username = res["userName"]
        password = res["passWord"]
        try:
            avatarUrl = res['avatarUrl']
        except:
            avatarUrl = ''
        logger.info('register page calling POST method.')
        logger.info('username : %s, password : %s, email : %s, avatarUrl : %s',username,password,email,avatarUrl)

        # result should be return to html page.
        db_res = db.addUser(username,password,email,avatarUrl)
        logger.info('resul: %s',json.dumps(db_res))
        return redirect("/")
    else:
        return render_template("register.html",name=None)

"""
Try to find user is exist in DB or not first,
if exist and password match, login success.
else login fails.
"""

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        res = request.form
        username = res["username"]
        password = res["password"]

        logger.info('username : %s, password : %s',username,password)

        user = db.findUser(username)

        if user == None:
            logger.warning('username : %s not found.', username)
            return jsonify({"error" : "Invalid username or password."}), 400
        if user.password == password:
            logger.info('username : %s password is match.', username)
            return jsonify(user.serialize()), 200
        
        logger.info('Invalid password.')
        return jsonify({'err':"Invalid user or password"}), 400
    return render_template("login.html",name=None)

"""
update user's information include password or email.
It shouldn't allow user to edit their username, but fix it later.
"""

@app.route("/update", methods=['POST'])
def update_user():
    res = request.form
    username = res["username"]
    field_to_update = res["field"]
    value = res["value"]
    logger.info('username : %s, field : %s, value : %s',username,field_to_update,value)

    db_res = db.updateUserInfor(username,field_to_update,value)

    if 'error' in db_res:
        logger.error('error : %s',json.dumps(db_res))
        return jsonify({'msg' : 'error'}), 400
    logger.info('Update successful.')
    return jsonify({'msg' : 'Update successful.'}), 200

# for user to delete themselves account, or for administrator uses.

@app.route("/delete", methods=['POST'])
def delete_user():
    res = request.form
    username = res["username"]
    
    logger.info('render delete page.')
    logger.info('username % s',username)

    # check user is exist or not first.
    db_res = db.deleteUser(username)

    if 'error' in db_res:
        logger.error(json.dumps(db_res))
        return jsonify({'msg' : json.loads(db_res)['error']}), 409
    
    logger.info('Delete user : %s successful.', username)
    return jsonify({'msg' : f"Deactivated '{username}' successful."}), 202

# for testing, normal user shouldn't has this authority.

@app.route("/find",methods=['GET'])
def find_user():
    logger.info('Render find page.')
    try:
        username = request.args.get('username')
        logger.info('username is %s',username)
    except:
        logger.info('No username parameter in request.')

    db_res = db.findUser(username)
    if 'error' in db_res:
        logger.error(json.dumps(db_res))
        return db_res

    return db_res, 200

@app.route("/findUserPrefix",methods = ['GET'])
def findUserPrefix():
    logger.info("findUserPrefix method called.")
    try:
        prefix = request.args.get('prefix')
        logger.info('prefix is %s : ', prefix)
    except:
        logger.info('No prefix parameter found.')
    
    db_res = db.findUserByPrefix(prefix)
    if 'error' in db_res:
        logger.info(json.dumps(db_res))

    return db_res, 200

"""
display list of cell phones.
"""
@app.route("/list/cellphone", methods = ["GET"])
def listPhone():
    return render_template("list.html",name=None)

# just for test.
@app.route("/hello", methods=["GET"])
def hello_world():
    print("hello world")
    return 'hello, world!'

if __name__ == "__main__":
    webbrowser.open_new("localhost:8080")
    app.run("localhost", 8080, debug=True)