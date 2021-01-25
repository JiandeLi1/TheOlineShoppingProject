from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key = True,nullable = False)
    username = Column(String(), unique = True, nullable = False)
    password = Column(String(), nullable = False)
    email = Column(String(), unique = True, nullable = False)
    avatarUrl = Column(String())

    def __init__(self,username,password,email,avatarUrl):
        self.username = username
        self.password = password
        self.email = email
        self.avatarUrl = avatarUrl
    
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'password' : self.password,
            'email' : self.email,
            'avatarUrl' : self.avatarUrl
        }

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer,primary_key = True,nullable = False)
    price = Column(Float(), nullable = False)
    itemName = Column(String(), unique = True, nullable = False)
    amount = Column(Integer(), nullable = False)
    itemImageUrl = Column(String())

    def __init__(self,price,itemName,amount,itemImageUrl):
        self.price = price
        self.itemName = itemName
        self.amount = amount
        self.itemImageUrl = itemImageUrl

    def __repr__(self):
        return '<itemName {}, price {}, amount {}, itemImageUrl{}>'.format(self.itemName,self.price,self.amount,self.itemImageUrl)
    
    def serialize(self):
        return {
            'itemName' : self.itemName,
            'price' : self.price,
            'amount' : self.amount,
            'itemImageUrl' : self.itemImageUrl
        }

class PurchaseRecord(Base):
    __tablename__ = 'purchaseHistries'

    id = Column(Integer,primary_key = True,nullable = False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable = False)
    itemName = Column(String(),nullable = False)
    amount = Column(Integer(),nullable = False)
    totalPrice = Column(Float(),nullable = False)
    itemImageUrl = Column(String())

    def __init__(self,user_id,itemName,amount,totalPrice,itemImageUrl):
        self.user_id = user_id
        self.itemName = itemName
        self.amount = amount
        self.totalPrice = totalPrice
        self.itemImageUrl = itemImageUrl

    def __repr__(self):
        return '<user_id {}, itemName {}, amount {}, totalPrice {}, itemImageUrl{}>'.format(self.user_id,self.itemName,self.amount,self.totalPrice,self.itemImageUrl)

    def serialize(self):
        return {
            'user_id' : self.user_id,
            'itemName' : self.itemName,
            'amount' : self.amount,
            'totalPrice' : self.totalPrice,
            'itemImageUrl' : self.itemImageUrl
        }

    


# code beblow for init tables in database.

def init():
    from sqlalchemy import create_engine
    engine = create_engine('postgresql+psycopg2://wiyeifpkilnddz:23594bc1b1a7382ba22476b4b84c39577eaa183c0f57b829a2eb1bd304b63452@ec2-52-0-65-165.compute-1.amazonaws.com/dfhrerbt81rcpc')

    from sqlalchemy.orm import sessionmaker
    session = sessionmaker()
    session.configure(bind = engine)
    Base.metadata.create_all(engine)

# This method is used to create tables in database.
# init()
