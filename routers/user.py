# All Users
from fastapi import APIRouter
from models.model import User
from models.database import db

router = APIRouter()

# Get All Users
@router.get("")
def all_users():
    return {"data": db }

# Get One User
@router.get("{user_id}")
def one_user(user_id: int):
    return {"data": db[user_id] } 

# Add One User
@router.post("")
def post_user(user: User):
    db.append(user)
    return {"data": "successfull!"}