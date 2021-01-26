from flask import Flask, render_template, request, redirect
import webbrowser
import json

app = Flask(__name__, template_folder="../templates", static_folder = "../static")

fake_users = {
    'xiaoming' : {'email' : 'xiaoming@gmail.com', 'password' : '12456'},
    'zhangsan' : {'email' : 'zhangsan@gmail.com','password' : '456123'},
    'jiande' : {'email' : 'jiande@gmail.com','password' : '321654'}
}

fake_product = {
    'iphone' : {'price' : 999.99, 'amount' : 50, 'itemImageUrl' : 'https://m.media-amazon.com/images/I/51m095zShrL._AC_SX466_.jpg'},
    'iphone12' : {'price' : 1299.99, 'amount' : 25, 'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'}
}

fake_purchaseHistory = {
    1 : [
        {'itemName' : 'iphone',
        'amount' : 12,
        'totalPrice' : 11999.88,
        'itemImageUrl' : 'https://m.media-amazon.com/images/I/51m095zShrL._AC_SX466_.jpg'},
        {'itemName' : 'iphone12',
        'amount' : 3,
        'totalPrice' : 3899.97,
        'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'}],
    2 : [{
        'itemName' : 'iphone12',
        'amount' : 8,
        'totalPrice' : 10399.92,
        'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'
    }]
}

fake_userIDNameMap = {
    'xiaoming' : 1,
    'jiande' : 2,
    'zhangsan' : 3
}

# Showing the home page.
@app.route("/", methods=["GET"])
def redirect_home():
    return render_template("index.html",name=None)

"""
check username is exist or not,
than check email is already used or not.
"""
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        res = request.form
        email = res["email"]
        username = res["userName"]
        password = res["passWord"]
        # result should be return to html page.
        if username in fake_users:
            return json.dumps({'status' : 'user already exist'}), 404
        for user,val in fake_users.items():
            if val['email'] == email:
                return json.dumps({'status' : 'email already exist.'}), 404
        return json.dumps({'status' : 'success','redirctUrl' : '/index.html'}), 200
        # print("here.")
        # return render_template("index.html",name=None)
    else:
        return render_template("test.html",name=None)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        res = request.form
        username = res["userName"]
        password = res["passWord"]
        for username in fake_users:
            if user['username'] == username and user['password'] == password:
                return json.dumps({'username' : username}), 200
        return json.dumps({'status' : 'user not found.'}), 404
    return render_template("login.html",name=None)

"""
suppose front end send json array to it.
and we check each product that user want to buy.
if itemName, price and remain amount are match for all products user want to buy. return success.
else return reason why checkout false.
"""
@app.route("/checkout",methods=['POST'])
def checkout():
    if(request.data):
        datas = request.get_json()
        for data in datas:
            itemFind = True
            priceMatch = True
            amountEnough = True
            if data['itemName'] in fake_product:
                if data['price'] != fake_product[data['itemName']]['price']:
                    priceMatch = False
                if data['amount'] > fake_product[data['itemName']]['amount']:
                    amountEnough = False
            else:
                itemFind = False

            if not itemFind:
                return json.dumps({'status' : 'Item %s not found.' % data['itemName']}), 404
            if not priceMatch:
                return json.dumps({'status' : '%s Price not match.' % data['itemName']}), 404
            if not amountEnough:
                return json.dumps({'status' : '%s Product not enough.' % data['itemName']}), 404
        return json.dumps({'status' : 'checkout success.'}), 200

"""
Check user's history by username,
If user is not exist, return username not exist.
If user don't have purchase history, reutrn it.
If user exist and has purchase history, return all of them.
"""
@app.route("/history",methods=['POST'])
def purchaseHistory():
    res = request.form
    username = res['username']
    if username in fake_userIDNameMap:
        userID = fake_userIDNameMap[username]
    else:
        return json.dumps({'status' : 'username not found.'}), 404
    if userID in fake_purchaseHistory:
        return json.dumps(fake_purchaseHistory[userID]), 200
    return json.dumps({'status' : 'user %s did has any purchase history.' % username}),404



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