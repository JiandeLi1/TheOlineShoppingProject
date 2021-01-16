from flask import Flask, render_template, request, redirect, jsonify
import webbrowser
import dbModule
import json

app = Flask(__name__, template_folder="templates", static_folder = "static")

# Showing the home page.
@app.route("/", methods=["GET"])
def redirect_home():
    return render_template("index.html",name=None)

@app.route("/register", methods=["POST", "GET"])
def register():
    """
    implment the register without store data, finish later maybe.
    """
    if request.method == "POST":
        res = request.form
        print(res)
        email = res["email"]
        username = res["userName"]
        password = res["passWord"]
        # result should be return to html page.
        res = dbModule.add_user(username,password,email)
        print(res)
        return redirect("/")
    else:
        return render_template("register.html",name=None)

@app.route("/login",methods=["POST"])
def login():
    if request.method == 'POST':
        res = requets.form
        username = res["username"]
        password = res["password"]
        
        db_result = json.leads(dbModule.find_user("username",username))
        user_data = list(db_result["user"])

        if len(user_data) > 0:
            if user_data[0]['password'] == password:
                return jsonify({'user':user_data[0]}), 200
            
        return jsonify({'err':"Invalid user or password"})

@app.route("/update", methods=['PUT'])
def update_user():
    res = requets.get_json()
    field_to_update = res['field']
    value = res['value']
    db_res = json.loads(dbModule.update_user(username,field_to_update,value))

    if len(db_res['user']) > 0:
        return jsonify({'msg' : 'Update Successful.'}), 202
    else:
        return jsonify({'err' : 'User invalid.'}), 400

@app.route("/delete", methods=['DELETE'])
def delete_user():
    res = requets.form
    username = res["username"]

    user_exist = (
        len(db_res = json.loads(dbModule.find_user('username',username))['user']) > 0
    )
    if user_exist:
        dbModule.delete_user("username",username)
        return jsonify({'msg' : f"Deactivated {user} successful."}), 202
    else:
        return jsonify({'err' : "User invalid"}), 409


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