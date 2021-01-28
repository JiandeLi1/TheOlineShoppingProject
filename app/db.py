from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from flask import jsonify
import data_models
import json
import logging

import time

# connect database.
engine = create_engine(
    'postgresql+psycopg2://wiyeifpkilnddz:23594bc1b1a7382ba22476b4b84c39577eaa183c0f57b829a2eb1bd304b63452@ec2-52-0-65-165.compute-1.amazonaws.com/dfhrerbt81rcpc',
    echo=True
)
print(engine.url.database)
Session_factory = scoped_session(sessionmaker(bind=engine))

# init logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logging.log',mode = 'w')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

"""
----------------- user data section -----------------------
"""
def addUser(username,password,email,avatarUrl):
    logger.info('addUser method is called.')
    session = Session_factory()
    try:
        user = data_models.User(
            username = username,
            password = password,
            email = email,
            avatarUrl = avatarUrl
        )
        session.add(user)
        session.commit()
        logger.info('Add user : %s successfully.',username)
        return json.dumps({'success' : "Add user success."})
    except Exception as e:
        session.rollback()
        logger.error('Add user : %s fails.',username)
        return json.dumps({'error' : str(e)})
    finally:
        session.close()

def updateUserInfor(username,field_to_update,value):
    logger.info('updateUserInfor method is called.')
    logger.info('Start getting mutex lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(nowait = False).filter_by(username = username).first()
    logger.info('Finish getting mutex lock.')

    if user == None:
        logger.error('User : %s not found',username)
        session.close()
        return json.dumps({'error' : 'Invalid user'})

    if hasattr(user,field_to_update):
        try:
            setattr(user,field_to_update,value)
            logger.info('Updating user: %s into table.', username)
            session.add(session.merge(user))
            session.commit()
            logger.info('Update user : %s successfuly.',username)
            return json.dumps({'success' : 'Update Successful.'})
        except Exception as e:
            session.rollback()
            logger.info('Update fails : %s',str(e))
            return json.dumps({'error' : str(e)})
        finally:
            session.close()
    else:
        logger.error('Fails to update.')
        return json.dumps({'error' : 'Fails to update.'})

def deleteUser(username):
    logger.info('deleteUser method is called.')
    logger.info('Start getting mutex lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(nowait = False).filter_by(username = username).first()
    logger.info('Finish gettting mutex lock.')

    if user == None:
        logger.error('User : %s not found',username)
        session.close()
        return json.dumps({'error' : 'Invalid user.'})

    try:
        logger.info('Tring to delete user: %s', username)
        session.delete(user)
        session.commit()
        logger.info('User : %s delete successfully.',username)
        return json.dumps({'success' : 'user is deleted.'})
    except Exception as e:
        session.rollback()
        logger.error(str(e))
        return json.dumps({'error' : str(e)})
    finally:
        session.close()

def findUser(username):
    logger.info('getUser method is called.')
    logger.info('Start getting share lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(nowait = False,read = True).filter_by(username = username).first()
    # print(user)

    if user == None:
        logger.info('username %s not found',username)
        session.close()
        return json.dumps({'error' : 'Invalid user.'})
    
    session.close()
    return json.dumps(user.serialize())

def findUserByPrefix(prefix):
    logger.info('findUserByPrefix method is called.')
    logger.info('Start getting share lock.')
    session = Session_factory()
    parameter = '{}%'.format(prefix)
    print(parameter)
    users = session.query(data_models.User).filter(data_models.User.username.like(parameter)).all()
    logger.info('finished getting share lock.')

    if users == None:
        logger.error('No users found.')
        return json.dumps({'error' : 'No users found.'})

    logger.info('Find prefix success, now return results.')
    return json.dumps(users,default = lambda x : x.serialize())

"""
------------------ product data section ---------------------------------
"""

def getAllProducts():
    logger.info('getAllProducts methods is called.')
    logger.info('start getting share lock.')
    session = Session_factory()
    items = session.query(data_models.Item).with_for_update(nowait = False,read = True).filter_by().all()
    logger.info('finish getting share lock.')

    if not items:
        logger.info('no items found.')
        session.close()
        return json.dumps({'error' : 'No products found.'})

    session.close()
    logger.info('Find all items from DB.')
    return json.dumps(items,default = lambda x : x.serialize())

def getProduct(itemName):
    logger.info('getProduct method is called.')
    logger.info('start getting share lock.')
    session = Session_factory()
    item = session.query(data_models.Item).with_for_update(nowait = False,read = True).filter_by(itemName = itemName).first()
    logger.info('finish getting share lock.')

    if item is None:
        logger.info('no item found.')
        session.close()
        return json.dumps({'error' : 'No products found.'})

    session.close()
    logger.info('Find product %s' % itemName)
    return json.dumps(item.serialize())

def addProduct(itemName,price,amount,itemImageUrl):
    logger.info('addProduct method is called.')

    session = Session_factory()
    try:
        item = data_models.Item(
            itemName = itemName,
            price = price,
            amount = amount,
            itemImageUrl = itemImageUrl
        )
        session.add(item)
        session.commit()
        logger.info('Add item : %s successfully.',itemName)
        return json.dumps({'status' : 'success'})
    except Exception as e:
        session.rollback()
        logger.error('Add user : %s fails.',itemName)
        return json.dumps({'status' : 'fails','description' : str(e)})
    finally:
        session.close()

def updateProducts(datas):
    logger.info('updateProducts method is called.')
    itemNames = []
    mp = {}
    for data in datas:
        itemNames.append(data['itemName'])
        mp[data['itemName']] = {'price' : data['price'], 'amount' : data['amount']}

    logger.info('start getting mutex lock.')
    session = Session_factory()
    items = session.query(data_models.Item).with_for_update(nowait = False,read = True).filter(data_models.Item.itemName.in_(itemNames)).all()

    for item in items:
        itemName = item.itemName
        if item.price != mp[itemName]['price']:
            session.rollback()
            session.close()
            return json.dumps({'status' : 'fails','description' : 'product %s price not match.' % itemName})
        if item.amount < mp[itemName]['amount']:
            session.rollback()
            session.close()
            return json.dumps({'status' : 'fails','description' : 'product %s amount not enough.' % itemName})
        item.amount-= mp[item.itemName]['amount']

    try:
        session.commit()
        logger.info('update succssfully.')
        return json.dumps({'status' : 'success','description' : 'update successfully.'})
    except Exception as e:
        logger(str(e))
        session.rollback()
        return json.dumps({'status' : 'fails','description' : str(e)})
    finally:
        session.close()

"""
----------------------- user purchase history -----------------------------
"""
def getPurchaseHistory(username):
    logger.info('getPurchaseHistory method is called.')
    logger.info('start getting share lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(nowait = False,read = True).filter_by(username = username).first()
    if user == None:
        logger.info('usernaem %s not found.' % username)
        session.close()
        return json.dumps({'status' : 'fails', 'description' : 'username not found.'})
    user_id = user.id
    username = user.username
    session.close()
    logger.info('finished get share lock.')

    logger.info('start getting share lock.')
    session = Session_factory()
    history = session.query(data_models.PurchaseRecord).with_for_update(nowait = False,read = True).filter_by(user_id = user_id).all()
    logger.info('finished get share lock.')

    if history == None:
        logger.info('user %s history not found.' % username)
        session.close()
        return json.dumps({'status' : 'fails', 'description' : 'user : %s history not found.' % username})
    
    logger.info('user : %s history find.')
    return json.dumps(history,default = lambda x : x.serialize())

def addPurchaseHistory(username,itemName,amount,totalPrice,itemImageUrl):
    logger.info('addPurchaseHistory method is called.')
    logger.info('start getting share lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(nowait = False,read = True).filter_by(username = username).first()
    logger.info('finished get share lock.')
    if user == None:
        logger.info('usernaem %s not found.' % username)
        session.close()
        return json.dumps({'status' : 'fails', 'description' : 'username not found.'})
    user_id = user.id
    username = user.username
    session.close()
    logger.info('release the share lock.')

    try:
        logger.info('start getting mutex lock.')
        session = Session_factory()
        history = data_models.PurchaseRecord(
            user_id = user_id,
            itemName = itemName,
            amount = amount,
            totalPrice = totalPrice,
            itemImageUrl = itemImageUrl
        )
        session.add(history)
        session.commit()
        logger.info('add user %s purchase history successful.' % username)
        return json.dumps({'status' : 'success'})
    except Exception as e:
        session.rollback()
        logger.info('add user %s purchase history fails.' % username)
        return json.dumps({'status' : 'fails'})
    finally:
        logger.info('release the mutex lock.')
        session.close()

