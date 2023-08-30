
from sqlalchemy import Column, String, Integer
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  relationship, DeclarativeBase, sessionmaker
import os 
from cryptography.fernet import Fernet 
import sqlalchemy as db

Base = declarative_base()
db_url = "sqlite:///./logininfo.db"


class LoginInfo(Base):
    __tablename__ = "logininfo"

    id = Column(Integer, index=True, primary_key=True)
    website = Column(String, unique=True)
    email = Column(String)
    hashed = Column(String)

def CreateEngine():
    engine = db.create_engine(db_url, echo=True)
    return engine


def add_data(website, email, hashed):
    engine = CreateEngine()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        info_data = LoginInfo(website, email, hashed)
        session.add(info_data)
        session.commit()
    
    except Exception as err:
        print("[!] Error Happened = {}".format(str(err)))



