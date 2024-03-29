
from sqlalchemy import Column, String, Integer, update
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  relationship, DeclarativeBase, sessionmaker
import sqlalchemy as db

Base = declarative_base()
db_url = "sqlite:///localfiles/logininfo.db"


#database model connection
class LoginInfo(Base):
    __tablename__ = "logininfo"

    id = Column(Integer, index=True, primary_key=True)
    website = Column(String, unique=True)
    email = Column(String)
    hashed = Column(String)

#creating and engine and a session object
def load_engine():
    engine = db.create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

#Processing input 
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
            print("--FUNC ADD DATA \n [!] Error Happened = {}".format(str(err)))
		
    
def UpdateData(website, new_password):
    session = load_engine()
    update_object = update(LoginInfo)
    try:
        update_object = update_object.where(LoginInfo.website==website)
        update_object = update_object.values(hashed=new_password)
        session.execute(update_object)
        session.commit()
        print("----UPDATED SUCCESS----")
        return True
    except Exception as err:
        print("[!] UPDATE FUNC FAILED: {}".format(err))
    



def GetData(query_search):
    session_ = load_engine()
    try:
            data = session_.query(LoginInfo).filter(LoginInfo.website == query_search)
    except Exception as err:
        print("[!] Error occured : {}".format(str(err)))
    return data


def DeleteAll():
    session = load_engine()
    try:
        confirm = input(">> ARE YOU REALLY SURE:?")
        if confirm.lower() == "yes":
            session.query(LoginInfo).delete()
            session.commit()
            print("----ALL LOGIN INFOS ARE DELETED----")
        else:
            print("---That was close---")
    except Exception as err:
        print("[!] DELETE FUNC FAILED \n\t--- Something went Wrong : \n\t--{}".format(str(err)))
        
def DeleteOneEntry(website):
    session = load_engine()
    try:
        session.query(LoginInfo).filter(LoginInfo.website==website).delete()
        session.commit()
        return True
    except Exception as err:
        print("[!] DELETE FUNC FAILED \n\t ---> Something Went Wrong \n\t--> {}".format(err))
    

def AccessData():
    session = load_engine()
    try:
        info = session.query(LoginInfo).all()
        return info

    except Exception as err:
        print("[!] Error happened: {}".format(str(err)))



    
