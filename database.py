
from sqlalchemy import Column, String, Integer
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  relationship, DeclarativeBase, sessionmaker
import os 
from cryptography.fernet import Fernet 
import sqlalchemy as db
import traceback

Base = declarative_base()
db_url = "sqlite:///./logininfo.db"


engine = db.create_engine(db_url)

class LoginInfo(Base):
    __tablename__ = "logininfo"

    id = Column(Integer, index=True, primary_key=True)
    website = Column(String, unique=True)
    email = Column(String)
    hashed = Column(String)


def load_engine():
    engine = db.create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class ProcessInformation():

    def __init__(self,website, email, hashed):
        self.website = website
        self.email = email 
        self.hashed = hashed

    def CreateEngine(self):
        engine = db.create_engine(db_url, echo=True)
        return engine

    def add_data(self):
        session = load_engine()
        try:
            info_data = LoginInfo(website=self.website, email=self.email, hashed=self.hashed)
            session.add(info_data)
            session.commit()
    
        except Exception as err:
            traceback.print_exc()
            print("--FUNC ADD DATA \n [!] Error Happened = {}".format(str(err)))
		

def GetData(query_search):
	session_ = load_engine()
	try:
	    data = session_.query(LoginInfo).filter(LoginInfo.website == query_search)
	except Exception as err:
	    traceback.print_exc()
	    print("[!] Error occured : {}".format(str(err)))
	return data



	
    
def AccessData():
    session = load_engine()
    try:
        info = session.query(LoginInfo).all()
        return info

    except Exception as err:
        print("[!] Error happened: {}".format(str(err)))



    
