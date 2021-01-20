from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from flask import jsonify
import data_models
import json
import logging

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

def addUser(username,password,email,avatarUrl):
    logger('addUser method is called.')
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
    user = findUser(username)

    if user == None:
        logger.error('User : %s not found',username)
        return json.dumps({'error' : 'Invalid user'})

    if hasattr(user,field_to_update):
        session = Session_factory()
        try:
            setattr(user,field_to_update,value)
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
    user = findUser(username)

    if user == None:
        logger.error('User : %s not found',username)
        return json.dumps({'error' : 'Invalid user.'})

    session = Session_factory()
    try:
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

def getUser(username):
    logger.info('getUser method is called.')
    user = findUser(username)

    if user == None:
        logger.info('username %s not found',username)
        return json.dumps({'error' : 'Invalid user.'})
    
    return json.dumps(user.serialize())

def findUser(username):
    logger.info('findUser method is called.')
    session = Session_factory()
    try:
        return session.query(data_models.User).filter_by(username = username).first()
    except:
        logger.info('username %s not found',username)
    finally:
        session.close()
    return None