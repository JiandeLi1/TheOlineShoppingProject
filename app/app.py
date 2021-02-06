from flask import Flask, render_template, request, redirect, jsonify
import webbrowser
import json
import os
import db
import logging

app = Flask(__name__, template_folder="../templates", static_folder = "../static")

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


# Showing the cart page.
@app.route("/cart", methods=["GET"])
def cart():
    return render_template("shoppingcart.html", name=None)
    

# Showing the checkout page.
@app.route("/checkout_page", methods=["GET"])
def checkout_page():
    return render_template("checkut.html",name=None)

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
        if 'success' in db_res:
            return json.dumps({'status' : 'success','redirctUrl' : '/'}), 200
        return json.dumps({'status' : 'fails','description' : 'Invalid username or password.'}), 200
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
        username = res["userName"]
        password = res["passWord"]

        logger.info('username : %s, password : %s',username,password)

        user = db.findUser(username)
        user_ditc = json.loads(user)

        if 'error' in user:
            logger.warning('username : %s not found.', username)
            return jsonify({'status' : 'fails',"description" : "Invalid username or password."}), 400
        if user_ditc['password'] == password:
            logger.info('username : %s password is match.', username)
            return json.dumps({'status' : 'success','username' : username, 'redirctUrl' : '/'}), 200
        
        logger.info('Invalid password.')
        return jsonify({'status' : 'fails',"description" : "Invalid username or password."}), 400
    return render_template("login.html",name=None)

"""
update user's information include password or email.
It shouldn't allow user to edit their username, but fix it later.
"""

@app.route("/update", methods=['POST'])
def update_user():
    res = request.form
    username = res["userName"]
    field_to_update = res["field"]
    value = res["value"]
    logger.info('username : %s, field : %s, value : %s',username,field_to_update,value)

    db_res = db.updateUserInfor(username,field_to_update,value)

    if 'error' in db_res:
        logger.error('error : %s',json.loads(db_res))
        return jsonify({'status' : 'fails',"description" : json.loads(db_res)}), 400
    logger.info('Update successful.')
    return json.dumps({'status' : 'success','redirctUrl' : '/'}), 200

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
        return jsonify({'status' : 'fails',"description" : json.loads(db_res)}), 400
    
    logger.info('Delete user : %s successful.', username)
    return json.dumps({'status' : 'success','redirctUrl' : '/'}), 200

# for testing, normal user shouldn't has this authority.

@app.route("/find",methods=['GET'])
def find_user():
    logger.info('Render find page.')
    try:
        username = request.args.get('userName')
        logger.info('username is %s',username)
    except:
        logger.info('No username parameter in request.')

    db_res = db.findUser(username)
    if 'error' in db_res:
        logger.error(json.dumps(db_res))
        return json.dumps({'status' : 'fails','description' : json.loads(db_res)}), 200

    return json.dumps({'status' : 'success','user' : json.loads(db_res)}), 200

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
----------------- product section -----------------------------
"""

## return array of json objects to frontend.
@app.route("/allProducts",methods=['GET'])
def getAllProducts():
    items = db.getAllProducts()
    if 'error' in items:
        logger.info('No product found.')
        return jsonify({'status' : 'error','description' : 'no product found.'}), 404
    logger.info('Find all products.')
    return items, 200

@app.route("/getProduct",methods=['POST'])
def getProduct():
    res = request.form
    itemName = res["itemName"]
    
    logger.info('trying to find product %s' % itemName)

    db_res = db.getProduct(itemName)

    if 'error' in db_res:
        logger.info('error happend.')
        return json.dumps({'status' : 'fails', 'description' : json.loads(db_res)}), 404
    
    logger.info('Product %s found.' % itemName)
    return json.dumps({'status' : 'success','item' : json.loads(db_res)}), 200

@app.route("/addProduct",methods=['POST'])
def addProduct():
    res = request.form
    itemName = res['itemName']
    price = res['price']
    amount = res['amount']
    itemImageUrl = res['itemImageUrl']

    logger.info('trying to add item %s to DB.' % itemName)

    db_res = db.addProduct(itemName,price,amount,itemImageUrl)
    data = json.loads(db_res)

    if data.get('status') == 'fails':
        return json.dumps({'status' : 'fails','description' : data}), 404
    return json.dumps({'status' : 'success'}), 200

@app.route("/updateProducts",methods=['POST'])
def updateProducts():
    if(request.data):
        datas = request.get_json()
        db_res = db.updateProducts(datas)

        if json.loads(db_res)['status'] == 'fails':
            logger.info('update fails')
            return db_res, 400
        logger.info('update success.')
        return db_res, 200

@app.route("/searchProduct",methods=['POST'])
def searchProduct():
    logger.info('search product page.')
    res = request.form
    try:
        itemName = res['itemName']
    except Exception as e:
        logger.info('No valid paramater found.')
        return json.dumps([]), 404

    if len(itemName) < 3:
        return json.dumps({'status' : 'error','description' : 'itemName too short.'}), 404

    db_res = db.findProductsByPortion(itemName)

    if 'error' in db_res:
        logger.info(json.dumps(db_res)), 404
    return db_res, 200

"""
Find product with same prefix, up to 5 product will be return.
For search bar to showing result without press.
"""
@app.route("/searchProductByPrefix",methods=['POST'])
def searchProductByPrefix():
    logger.info('search product page.')
    res = request.form
    try:
        itemName = res['itemName']
    except Exception as e:
        logger.info('No valid parameter found.')
        return json.dumps([]), 404

    if len(itemName) == 0:
        return json.dumps({'status' : 'error','description' : 'empty prefix not allow.'}), 404

    db_res = db.findProductsByPrefix(itemName)

    if 'error' in db_res:
        logger.info(json.dumps(db_res)), 404
    return db_res, 200

@app.route("/listProduct",methods=['GET'])
def listProduct():
        db_res = db.getAllProducts()
        return db_res, 200
    # return json.dumsp({'status' : 'fails'}), 404

@app.route("/search", methods=["GET"])
def redirect_search():
    return render_template("search.html",name=None)

"""
--------------------------- user purchase history ---------------------------------------
"""

@app.route("/getHistory",methods=['POST'])
def getPurchaseHistory():
    res = request.form
    try:
        username = res['userName']
    except Exception as e:
        logger.info('username does not exist.')
        return json.dumps({'status' : 'error', 'description' : 'lack of username'}), 400

    db_res = db.getPurchaseHistory(username)
    data = json.loads(db_res)

    if not data:
        logger.info('Can not find user %s history' % username)
        return json.dumps({'status' : 'fails', 'description' : 'No user history Found.'})

    logger.info('user hisotry is found.')

    return json.dumps({'status' : 'success','history' : data})

@app.route("/addHistory",methods=['POST'])
def addPurchaseHistory():
    res = request.form
    try:
        username = res['userName']
        itemName = res['itemName']
        amount = res['amount']
        totalPrice = res['totalPrice']
        itemImageUrl = res['itemImageUrl']
    except Exception as e:
        logger.info('username does not exist.')
        return json.dumps({'status' : 'error', 'description' : 'lack of username'}), 400

    db_res = db.addPurchaseHistory(username,itemName,amount,totalPrice,itemImageUrl)
    data = json.loads(db_res)

    if data.get('status') == 'fails':
        logger.info('add user : %s history fails.' % username)
        return db_res, 400

    logger.info('add user : %s history successfully.' % username)

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