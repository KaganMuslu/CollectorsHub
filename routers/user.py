from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from models.model import PydanticUser, User, UpdateUser, get_db
from sqlalchemy.orm import Session

router = APIRouter()

# if user exist returns user
def user_db_query(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if (user == None):
        raise HTTPException(status_code=404, detail="User not found!")
    else:
        return user

# Get All Users
@router.get("")
def all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"data": users }

# Add One User
@router.post("", status_code=201)
def post_user(user: PydanticUser, db: Session = Depends(get_db)):
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    return {"data": "successfull!"}

# Get One User
@router.get("/{user_id}")
def get_one_user(user_id: int = Path(description="The ID of the user"), db: Session = Depends(get_db)):
    user = user_db_query(db, user_id)
    
    return {"data": user }

# Delete One User
@router.delete("/{user_id}")
def delete_one_user(user_id: int = Path(description="The ID of the user"), db: Session = Depends(get_db)):
    user = user_db_query(db, user_id)
    db.delete(user)
    db.commit()
    
    return {"data": "deleted!"}

# Update One User
@router.put("/{user_id}")
def update_one_category(user: UpdateUser, user_id: int = Path(description="The ID of the user"), db: Session = Depends(get_db)):
    old_user = user_db_query(db, user_id)

    update_data = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(old_user, key, value)

    db.commit()
    new_user = db.query(User).filter(User.id == user_id).first()

    return {"data": new_user}
