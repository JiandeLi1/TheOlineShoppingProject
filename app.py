from flask import Flask, render_template, request, redirect, jsonify
import webbrowser
import json
import os
import db

app = Flask(__name__, template_folder="templates", static_folder = "static")

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from data_models import User

# Showing the home page.
@app.route("/", methods=["GET"])
def redirect_home():
    return render_template("index.html",name=None)

"""
Register page rander, if user register, it will return a message to tell user it is successful or any error occurs.
"""
@app.route("/register", methods=["POST", "GET"])
def register():
    """
    implment the register without store data, finish later maybe.
    """
    if request.method == "POST":
        res = request.form
        email = res["email"]
        username = res["userName"]
        password = res["passWord"]
        try:
            avatarUrl = res['avatarUrl']
        except:
            avatarUrl = ''

        # result should be return to html page.
        db_res = db.addUser(username,password,email,avatarUrl)
        print(db_res)
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

        # user = db.session.query(User).filter_by(username = username).first()
        user = db.findUser(username)

        if user == None:
            print("no user find.")
            return jsonify({"error" : "Invalid username or password."}), 400
        if user.password == password:
            print("find user.")
            return jsonify(user.serialize()), 200
            
        print("invalid password")
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
    db_res = db.updateUserInfor(username,field_to_update,value)

    if 'error' in db_res:
        return jsonify({'msg' : 'error'}), 400
    return jsonify({'msg' : 'Update successful.'}), 200

# for user to delete themselves account, or for administrator uses.

@app.route("/delete", methods=['POST'])
def delete_user():
    res = request.form
    username = res["username"]
    
    # check user is exist or not first.
    db_res = db.deleteUser(username)

    if 'error' in db_res:
        return jsonify({'msg' : json.loads(db_res)['error']}), 409
    
    return jsonify({'msg' : f"Deactivated '{username}' successful."}), 202

# for testing, normal user shouldn't has this authority.

@app.route("/find",methods=['GET'])
def find_user():
    username = request.args.get('username')

    db_res = db.getUser(username)
    if 'error' in db_res:
        return db_res

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