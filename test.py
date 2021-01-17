from flask import Flask, render_template, request, redirect
import webbrowser

app = Flask(__name__, template_folder="templates", static_folder = "static")

# Showing the home page.
@app.route("/", methods=["GET"])
def redirect_home():
    return render_template("index.html",name=None)

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        res = request.form
        email = res["email"]
        username = res["userName"]
        password = res["passWord"]
        # result should be return to html page.
        print(username, password, email)
        return redirect("/")
    else:
        return render_template("register.html",name=None)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        res = request.form
        username = res["userName"]
        password = res["passWord"]
        print(username, password)
        return render_template("index.html",name=None)
    return render_template("login.html",name=None)

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