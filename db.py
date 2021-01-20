from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from flask import jsonify
import data_models
import json

engine = create_engine(
    'postgresql+psycopg2://wiyeifpkilnddz:23594bc1b1a7382ba22476b4b84c39577eaa183c0f57b829a2eb1bd304b63452@ec2-52-0-65-165.compute-1.amazonaws.com/dfhrerbt81rcpc',
    echo=True
)
print(engine.url.database)
Session_factory = scoped_session(sessionmaker(bind=engine))

def addUser(username,password,email,avatarUrl):
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
        return json.dumps({'success' : "Add user success."})
    except Exception as e:
        session.rollback()
        return json.dumps({'error' : str(e)})
    finally:
        session.close()

def updateUserInfor(username,field_to_update,value):
    user = findUser(username)

    if user == None:
        return json.dumps({'error' : 'Invalid user'})

    if hasattr(user,field_to_update):
        session = Session_factory()
        try:
            setattr(user,field_to_update,value)
            session.add(session.merge(user))
            session.commit()
            return json.dumps({'success' : 'Update Successful.'})
        except Exception as e:
            session.rollback()
            return json.dumps({'error' : str(e)})
        finally:
            session.close()
    else:
        return json.dumps({'error' : 'Fails to update.'})

def deleteUser(username):
    user = findUser(username)

    if user == None:
        return json.dumps({'error' : 'Invalid user.'})

    session = Session_factory()
    try:
        session.delete(user)
        session.commit()
        return json.dumps({'success' : 'user is deleted.'})
    except Exception as e:
        session.rollback()
        return json.dumps({'error' : str(e)})
    finally:
        session.close()

def getUser(username):
    user = findUser(username)

    if user == None:
        return json.dumps({'error' : 'Invalid user.'})
    
    return json.dumps(user.serialize())

def findUser(username):
    session = Session_factory()
    try:
        return session.query(data_models.User).filter_by(username = username).first()
    finally:
        session.close()
    return None