from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key = True,nullable = False)
    username = Column(String())
    password = Column(String())
    email = Column(String())

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
    
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'password' : self.password,
            'email' : self.email
        }

# code beblow for init table in database.

# from sqlalchemy import create_engine
# engine = create_engine('postgresql+psycopg2://wiyeifpkilnddz:23594bc1b1a7382ba22476b4b84c39577eaa183c0f57b829a2eb1bd304b63452@ec2-52-0-65-165.compute-1.amazonaws.com/dfhrerbt81rcpc')

# from sqlalchemy.orm import sessionmaker
# session = sessionmaker()
# session.configure(bind = engine)
# Base.metadata.create_all(engine)
