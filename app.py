from flask import Flask, render_template, request, redirect, jsonify
import webbrowser
import dbModule
import json

app = Flask(__name__, template_folder="templates", static_folder = "static")

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
        # result should be return to html page.
        db_res = dbModule.add_user(username,password,email)
        return redirect("/")
    else:
        return render_template("register.html",name=None)

"""
Try to find user is exist in DB or not first,
if exist and password match, login success.
else login fails.
"""
@app.route("/login",methods=["POST"])
def login():
    if request.method == 'POST':
        res = request.form
        username = res["username"]
        password = res["password"]
        
        db_result = json.loads(dbModule.find_user("username",username))
        user_data = list(db_result["user"])

        if len(user_data) > 0:
            if user_data[0]['password'] == password:
                return jsonify({'user':user_data[0]}), 200
            
        return jsonify({'err':"Invalid user or password"})

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
    db_res = json.loads(dbModule.update_user(username,field_to_update,value))

    if 'error' in db_res:
        return db_res

    if db_res['status'] == 'success':
        return jsonify({'msg' : 'Update Successful.'}), 202
    else:
        return jsonify({'err' : 'User invalid.'}), 400

# for user to delete themselves account, or for administrator uses.
@app.route("/delete", methods=['POST'])
def delete_user():
    res = request.form
    username = res["username"]
    
    # check user is exist or not first.
    user_exist = (
        len(list(json.loads(dbModule.find_user('username',username))['user'])) > 0
    )
    if user_exist:
        db_res = json.loads(dbModule.delete_user(username))
        if 'error' in db_res:
            return db_res
        elif db_res["status"] == 'fails':
            return db_res
        return jsonify({'msg' : f"Deactivated '{username}' successful."}), 202
    else:
        return jsonify({'err' : "User invalid"}), 409

# for testing, normal user shouldn't has this authority.
@app.route("/find",methods=['GET'])
def find_user():
    username = request.args.get('username')
    print(username)

    db_res = json.loads(dbModule.find_user('username',username))
    if 'error' in db_res:
        return db_res
    user_data = list(db_res['user'])

    if len(user_data) > 0:
        return jsonify({'user' : user_data[0]}), 200
    return jsonify({'error' : 'Invalid user name.'})

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