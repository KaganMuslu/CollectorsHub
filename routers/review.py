from fastapi import APIRouter, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from models.model import Review, UpdateReview
from models.database import db

router = APIRouter()


# Get All Reviews
@router.get("")
def all_reviews():
    return {"data": db["reviews"] }

# Add One Review
@router.post("", status_code=201)
def post_review(review: Review):
    db["reviews"].append(review)
    return {"data": "successfull!"}

# Get One Review
@router.get("/{review_id}")
def get_one_review(review_id: int = Path(description="The ID of the Review") ):
    if review_id >= len(db["reviews"]):
        raise HTTPException(status_code=404, detail="Review not found!")
    
    return {"data": db["reviews"][review_id] } 

# Delete One Review
@router.delete("/{review_id}")
def delete_one_review(review_id: int = Path(description="The ID of the Review") ):
    if review_id >= len(db["reviews"]):
        raise HTTPException(status_code=404, detail="Review not found!")
    
    db["reviews"].remove(db["reviews"][review_id])
    return {"data": "deleted!"}

# Update One Review
@router.put("/{review_id}")
def update_one_category(review: UpdateReview, review_id: int = Path(description="The ID of the Review")):
    if review_id >= len(db["reviews"]):
        raise HTTPException(status_code=404, detail="Review not found!")

    old_review = db["reviews"][review_id]
    update_review = review.dict(exclude_unset=True)
    new_review = old_review.copy(update=update_review)

    db["reviews"][review_id] = jsonable_encoder(new_review)

    return {"data": new_review}
