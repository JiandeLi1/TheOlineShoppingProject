from flask import Flask, render_template, request, redirect
import webbrowser
import json

app = Flask(__name__, template_folder="../templates", static_folder = "../static")

# fake_users = {
#     'xiaoming' : {'email' : 'xiaoming@gmail.com', 'password' : '12456'},
#     'zhangsan' : {'email' : 'zhangsan@gmail.com','password' : '456123'},
#     'jiande' : {'email' : 'jiande@gmail.com','password' : '321654'}
# }

fake_product = {
   'iphone': {'price' : 999.99, 'amount' : 50, 'itemImageUrl' : 'https://m.media-amazon.com/images/I/51m095zShrL._AC_SX466_.jpg'},
  'iphone12':{'price' : 1299.99, 'amount' : 25, 'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'}
}

fake_users = [
    {
        'id' : 1,
        'userName' : 'xiaoming',
        'email' : 'xiaoming@gmail.com',
        'passWord' : '123456'
    },
    {
        'id' : 2,
        'userName' : 'zhangsan',
        'email' : 'zhangsan@gmail.com',
        'passWord' : '654321'
    },
    {
        'id' : 3,
        'userName' : 'jiande',
        'email' : 'jiande@gmail.com',
        'passWord' : '123456'
    }
]

fake_products = [
    {
        'itemName' : 'iphone',
        'price' : 999.99,
        'amount' : 50,
        'itemImageUrl' : 'https://m.media-amazon.com/images/I/51m095zShrL._AC_SX466_.jpg'
    },
    {
        'itemName' : 'iphone12',
        'price' : 1299.99,
        'amount' : 25,
        'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'
    }
]

fake_purchaseHistory = [
    {
        'id' : 1,
        'user_id' : 1,
        'itemName' : 'iphone',
        'amount' : 12,
        'totalPrice' : 11999.88,
        'itemImageUrl' : 'https://m.media-amazon.com/images/I/51m095zShrL._AC_SX466_.jpg'
    },
    {
        'id' : 2,
        'user_id' : 1,
        'itemName' : 'iphone12',
        'amount' : 3,
        'totalPrice' : 3899.97,
        'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'
    },
    {
        'id' : 3,
        'user_id' : 2,
        'itemName' : 'iphone12',
        'amount' : 8,
        'totalPrice' : 10399.92,
        'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'
    }
]

# fake_purchaseHistory = {
#     1 : [
#         {'itemName' : 'iphone',
#         'amount' : 12,
#         'totalPrice' : 11999.88,
#         'itemImageUrl' : 'https://m.media-amazon.com/images/I/51m095zShrL._AC_SX466_.jpg'},
#         {'itemName' : 'iphone12',
#         'amount' : 3,
#         'totalPrice' : 3899.97,
#         'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'}],
#     2 : [{
#         'itemName' : 'iphone12',
#         'amount' : 8,
#         'totalPrice' : 10399.92,
#         'itemImageUrl' : 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-12-pro-family-hero?wid=940&amp;hei=1112&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1604021663000'
#     }]
# }

# Showing the home page.
@app.route("/", methods=["GET"])
def redirect_home():
    return render_template("index.html", name=None)

@app.route("/search", methods=["GET"])
def redirect_search():
    return render_template("search.html",name=None)

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
        print(username," ",password)
        # result should be return to html page.
        for user in fake_users:
            if user['userName'] == username:
                return json.dumps({'status' : 'fails', 'description' : 'username already exist.'}), 404
            if user['email'] == email:
                return json.dumps({'status' : 'fails', 'description' : 'email already exist.'}), 404
        return json.dumps({'status' : 'success','redirctUrl' : '/'}), 200
        # print("here.")
        # return render_template("index.html",name=None)
    else:
        return render_template("register.html",name=None)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        res = request.form
        username = res["userName"]
        password = res["passWord"]
        print(username," ",password)
        for user in fake_users:
            if user['userName'] == username and user['passWord'] == password:
                return json.dumps({'status' : 'success','username' : username, 'redirctUrl' : '/'}), 200
        return json.dumps({'status' : 'fails','description' : 'user not found.'}), 404
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
            itemFind = False
            priceMatch = False
            amountEnough = False

            for item in fake_products:
                if item['itemName'] == data['itemName']:
                    itemFind = True
                    if item['price'] == data['price']:
                        priceMatch = True
                    if item['amount'] >= data['amount']:
                        amountEnough = True

            if not itemFind:
                return json.dumps({'status' : 'fails', 'description' : 'Item %s not found.' % data['itemName']}), 404
            if not priceMatch:
                return json.dumps({'status' : 'fails','description' : '%s Price not match.' % data['itemName']}), 404
            if not amountEnough:
                return json.dumps({'status' : 'fails','description' : '%s Product not enough.' % data['itemName']}), 404
        return json.dumps({'status' : 'success','redirctUrl' : '/'}), 200

@app.route("/listProduct",methods=['GET'])
def listProduct():
        return json.dumps(fake_products), 200
        # return json.dumps(fake_product), 200
    # return json.dumsp({'status' : 'fails'}), 404

@app.route("/getProduct",methods=['POST'])
def getProduct():
    res = request.form
    itemName = res['itemName']
    for item in fake_products:
        if item['itemName'] == itemName:
            return json.dumps(item), 200
    
    return json.dumps({'status' : 'fails'}), 404

@app.route("/searchProduct",methods=['POST'])
def searchProduct():
    res = request.form
    partionName = res['itemName']

    if len(partionName) < 3:
        return json.dumps({'status' : 'error','description' : 'itemName too short.'}), 404

    item_list = []

    for item in fake_products:
        if partionName in item['itemName']:
            item_list.append(item)
    print(len(item_list))
    return json.dumps(item_list), 200


"""
Check user's history by username,
If user is not exist, return username not exist.
If user don't have purchase history, reutrn it.
If user exist and has purchase history, return all of them.
"""
@app.route("/getHistory",methods=['POST'])
def getHistory():
    res = request.form
    username = res['userName']
    userID = -1
    for user in fake_users:
        if user['userName'] == username:
            userID = user['id']
    
    if userID == -1:
        return json.dumps({'status' : 'fails','description' : 'username not found.'}), 404

    history_list = []

    for his in fake_purchaseHistory:
        if his['user_id'] == userID:
            history_list.append(his)

    return json.dumps(history_list)



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