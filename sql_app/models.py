from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base 

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

class Exercises(Base):
    __tablename__ = 'exercises'

    exercise_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String) 
    
