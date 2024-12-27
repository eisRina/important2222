from fastapi import FastAPI
from pydantic import BaseModel,EmailStr, Field
from sqlalchemy import Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PlayerAccount(Base):
    __tableName__ = 'Player_data'
    
    id = Column(Integer,primary_key = True,index = True)
    user_name = Column(String, unique = True, index= True)
    email = Column(String, unique= True, index= True)
    hash_password = Column(String)
    
    
class CreateAccount(BaseModel):
    user_name: str = Field(..., min_length= 5, max_length= 15)
    email = EmailStr
    password : str = Field(...,min_length = 7)
    
    class Config():
        mode = True
        

