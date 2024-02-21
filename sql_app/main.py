from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

class Users(BaseModel):
    username: str
    password: str
    
class Exercises(BaseModel):
    name: str

    