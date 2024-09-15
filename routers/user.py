# All Users
from typing import Optional
from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel
from models.model import Gender, User
from models.database import db

router = APIRouter()

class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    gender: Optional[Gender] = None

# Get All Users
@router.get("")
def all_users():
    return {"data": db }

# Add One User
@router.post("")
def post_user(user: User):
    db.append(user)
    return {"data": "successfull!"}

# Get One User
@router.get("/{user_id}")
def get_one_user(user_id: int = Path(description="The ID of the user") ):
    if user_id >= len(db):
        raise HTTPException(status_code=404, detail="User not found!")
    
    return {"data": db[user_id] } 

# Delete One User
@router.delete("/{user_id}")
def delete_one_user(user_id: int = Path(description="The ID of the user") ):
    if user_id >= len(db):
        raise HTTPException(status_code=404, detail="User not found!")
    
    db.remove(db[user_id])
    return {"data": "deleted!"}

# Update One User
@router.put("/{user_id}")
def update_one_user(user:UpdateUser, user_id: int = Path(description="The ID of the user")):
    if user_id >= len(db):
        raise HTTPException(status_code=404, detail="User not found!")

    oldUser = db[user_id]
    
    if user.username is not None:
        oldUser.username = user.username
    if user.password is not None:
        oldUser.password = user.password
    if user.gender is not None:
        oldUser.gender = user.gender

    return {"data": db[user_id] }
