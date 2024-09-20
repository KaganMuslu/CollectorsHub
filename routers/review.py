from fastapi import APIRouter, Depends, HTTPException, Path
from models.pydantic import PydanticReview, UpdateReview
from models.model import Review, get_db
from sqlalchemy.orm import Session

router = APIRouter()

# If review exist returns review
def review_db_query(db, review_id):
    review = db.query(Review).filter(Review.id == review_id).first()
    if (review == None):
        raise HTTPException(status_code=404, detail="Review not found!")
    else:
        return review

# Get All Reviews
@router.get("")
def all_reviews(limit: int = 10, skip: int = 0, db: Session = Depends(get_db)):
    reviews = db.query(Review).offset(skip).limit(limit).all()
    return {"data": reviews}

# Add One Review
@router.post("", status_code=201)
def post_review(review: PydanticReview, db: Session = Depends(get_db)):
    new_review = Review(**review.model_dump())
    db.add(new_review)
    db.commit()
    return {"data": "successfull!"}

# Get One Review
@router.get("/{review_id}")
def get_one_review(review_id: int = Path(description="The ID of the Review"), db: Session = Depends(get_db)):
    review = review_db_query(db, review_id)
    
    return {"data": review} 

# Delete One Review
@router.delete("/{review_id}")
def delete_one_review(review_id: int = Path(description="The ID of the Review"), db: Session = Depends(get_db)):
    review = review_db_query(db, review_id)
    db.delete(review)
    db.commit()
    
    return {"data": "deleted!"}

# Update One Review
@router.put("/{review_id}")
def update_one_category(review: UpdateReview, review_id: int = Path(description="The ID of the Review"), db: Session = Depends(get_db)):
    old_review = review_db_query(db, review_id)

    update_data = review.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(old_review, key, value)

    db.commit()
    new_user = db.query(Review).filter(Review.id == review_id).first()

    return {"data": new_user}
