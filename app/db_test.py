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
handler = logging.FileHandler('logging.log',mode = 'a')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def test1(username,field_to_update,value):
    logger.info('test1 method is called.')
    logger.info('test1 starting get lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(nowait = False).filter_by(username = username).first()
    logger.info('test1 finish get lock.')
    logger.info('start sleep 5 seconds.')
    time.sleep(5)
    logger.info('finish sleep 5 seconds.')

    if user == None:
        logger.error('User : %s not found',username)
        session.close()
        return json.dumps({'error' : 'Invalid user'})

    if hasattr(user,field_to_update):
        try:
            setattr(user,field_to_update,value)
            session.add(session.merge(user))
            session.commit()
            logger.info('release lock.')
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

def test2(username,field_to_update,value):
    logger.info('test2 method is called.')
    logger.info('test2 start sleep 2 seconds.')
    time.sleep(2)
    logger.info('test2 finish sleep 2 seconds.')
    logger.info('test2 starting get lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(nowait = False).filter_by(username = username).first()
    logger.info('test2 finish get lock.')

    if user == None:
        logger.error('User : %s not found',username)
        session.close()
        return json.dumps({'error' : 'Invalid user'})

    if hasattr(user,field_to_update):
        try:
            setattr(user,field_to_update,value)
            session.add(session.merge(user))
            session.commit()
            logger.info('release lock.')
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

def test3(username):
    logger.info('test3 method is call.')
    logger.info('test3 start getting lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(read = True,nowait = False).filter_by(username = username).first()
    logger.info('test3 finish get lock.')
    logger.info('test3 starting sleep 3 seconds.')
    time.sleep(3)
    logger.info('test3 finished sleep.')

    if user == None:
        logger.error('User : %s not found',username)
        session.close()
        return json.dumps({'error' : 'Invalid user'})

    session.close()
    return json.dumps(user.serialize())

def test4(username):
    print("db_test test4 is called.")
    logger.info('test4 method is call.')
    logger.info('test4 start getting lock.')
    session = Session_factory()
    user = session.query(data_models.User).with_for_update(read = True,nowait = False).filter_by(username = username).first()
    logger.info('test4 finish get lock.')

    if user == None:
        logger.error('User : %s not found',username)
        session.close()
        return json.dumps({'error' : 'Invalid user'})

    session.close()
    return json.dumps(user.serialize())

