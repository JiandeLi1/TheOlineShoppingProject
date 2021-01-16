from flask import Flask, render_template, request, redirect
import webbrowser
import sqlTest

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
        res = sqlTest.add_user(username,password,email)
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
        
        db_result = json.leads(sqlTest)

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