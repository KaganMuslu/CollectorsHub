from fastapi import APIRouter, HTTPException, Path
from models.model import User, UpdateUser
from models.database import db_users

router = APIRouter()


# Get All Users
@router.get("")
def all_users():
    return {"data": db_users }

# Add One User
@router.post("")
def post_user(user: User):
    db_users.append(user)
    return {"data": "successfull!"}

# Get One User
@router.get("/{user_id}")
def get_one_user(user_id: int = Path(description="The ID of the user") ):
    if user_id >= len(db_users):
        raise HTTPException(status_code=404, detail="User not found!")
    
    return {"data": db_users[user_id] } 

# Delete One User
@router.delete("/{user_id}")
def delete_one_user(user_id: int = Path(description="The ID of the user") ):
    if user_id >= len(db_users):
        raise HTTPException(status_code=404, detail="User not found!")
    
    db_users.remove(db_users[user_id])
    return {"data": "deleted!"}

# Update One User
@router.put("/{user_id}")
def update_one_user(user:UpdateUser, user_id: int = Path(description="The ID of the user")):
    if user_id >= len(db_users):
        raise HTTPException(status_code=404, detail="User not found!")

    oldUser = db_users[user_id]
    
    if user.username is not None:
        oldUser.username = user.username
    if user.password is not None:
        oldUser.password = user.password
    if user.gender is not None:
        oldUser.gender = user.gender

    return {"data": db_users[user_id] }
