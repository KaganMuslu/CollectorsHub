from fastapi import APIRouter, Depends, HTTPException, Path
from models.model import Category, PydanticCategory, UpdateCategory, get_db
from sqlalchemy.orm import Session

router = APIRouter()

# If category exist returns category
def category_db_query(db, category_id):
    category = db.query(Category).filter(Category.id == category_id).first()
    if (category == None):
        raise HTTPException(status_code=404, detail="Category not found!")
    else:
        return category


# Get All Categories
@router.get("")
def all_categories(db: Session = Depends(get_db)):
    return {"data": db.query(Category).all()}

# Add One Category
@router.post("", status_code=201)
def post_category(category: PydanticCategory, db: Session = Depends(get_db)):
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    return {"data": "successfull!"}

# Get One Category
@router.get("/{category_id}")
def get_one_category(category_id: int = Path(description="The ID of the category"), db: Session = Depends(get_db)):
    category = category_db_query(db, category_id)
    
    return {"data": category} 

# Delete One Category
@router.delete("/{category_id}")
def delete_one_category(category_id: int = Path(description="The ID of the category"), db: Session = Depends(get_db)):
    category = category_db_query(db, category_id)
    db.delete(category)
    db.commit()
    
    return {"data": "deleted!"}

# Update One Category
@router.put("/{category_id}")
def update_one_category(category: UpdateCategory, category_id: int = Path(description="The ID of the category"), db: Session = Depends(get_db)):
    old_category = category_db_query(db, category_id)

    update_data = category.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(old_category, key, value)

    db.commit()
    new_category = db.query(Category).filter(Category.id == category_id).first()

    return {"data": new_category}
