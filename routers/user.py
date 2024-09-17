from fastapi import APIRouter, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from models.model import User, UpdateUser
from models.database import db_users

router = APIRouter()


# Get All Users
@router.get("")
def all_users():
    return {"data": db_users }

# Add One User
@router.post("", status_code=201)
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
def update_one_category(product: UpdateUser, user_id: int = Path(description="The ID of the user")):
    if user_id >= len(db_users):
        raise HTTPException(status_code=404, detail="User not found!")

    old_user = db_users[user_id]
    update_user = product.dict(exclude_unset=True)
    new_user = old_user.copy(update=update_user)

    db_users[user_id] = jsonable_encoder(new_user)

    return {"data": new_user}
