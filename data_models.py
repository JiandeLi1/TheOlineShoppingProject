from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key = True,nullable = False)
    username = Column(String(), unique = True, nullable = False)
    password = Column(String(), nullable = False)
    email = Column(String(), unique = True, nullable = False)

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

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer,primary_key = True,nullable = False)
    price = Column(Float(), nullable = False)
    itemName = Column(String(), unique = True, nullable = False)
    amount = Column(Integer(), nullable = False)

    def __init__(self,price,itemName,amount):
        self.price = price
        self.itemName = itemName
        self.amount = amount

    def __repr__(self):
        return '<itemName {}, price {}, amount {}>'.format(self.itemName,self.price,self.amount)
    
    def serialize(self):
        return {
            'itemName' : self.itemName,
            'price' : self.price,
            'amount' : self.amount
        }

class PurchaseRecord(Base):
    __tablename__ = 'purchaseHistries'

    id = Column(Integer,primary_key = True,nullable = False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable = False)
    itemName = Column(String(),nullable = False)
    amount = Column(Integer(),nullable = False)
    totalPrice = Column(Float(),nullable = False)

    def __init__(self,user_id,itemName,amount,totalPrice):
        self.user_id = user_id
        self.itemName = itemName
        self.amount = amount
        self.totalPrice = totalPrice

    def __repr__(self):
        return '<user_id {}, itemName {}, amount {}, totalPrice {}>'.format(self.user_id,self.itemName,self.amount,self.totalPrice)

    def serialize(self):
        return {
            'user_id' : self.user_id,
            'itemName' : self.itemName,
            'amount' : self.amount,
            'totalPrice' : self.totalPrice
        }

    


# code beblow for init table in database.

def init():
    from sqlalchemy import create_engine
    engine = create_engine('postgresql+psycopg2://wiyeifpkilnddz:23594bc1b1a7382ba22476b4b84c39577eaa183c0f57b829a2eb1bd304b63452@ec2-52-0-65-165.compute-1.amazonaws.com/dfhrerbt81rcpc')

    from sqlalchemy.orm import sessionmaker
    session = sessionmaker()
    session.configure(bind = engine)
    Base.metadata.create_all(engine)

# init()
