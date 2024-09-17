from fastapi import APIRouter, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from models.model import Category, UpdateCategory
from models.database import db_categories

router = APIRouter()


# Get All Categories
@router.get("")
def all_categories():
    return {"data": db_categories }

# Add One Category
@router.post("", status_code=201)
def post_category(category: Category):
    db_categories.append(category)
    return {"data": "successfull!"}

# Get One Category
@router.get("/{category_id}")
def get_one_category(category_id: int = Path(description="The ID of the category") ):
    if category_id >= len(db_categories):
        raise HTTPException(status_code=404, detail="Category not found!")
    
    return {"data": db_categories[category_id] } 

# Delete One Category
@router.delete("/{category_id}")
def delete_one_category(category_id: int = Path(description="The ID of the category") ):
    if category_id >= len(db_categories):
        raise HTTPException(status_code=404, detail="Category not found!")
    
    db_categories.remove(db_categories[category_id])
    return {"data": "deleted!"}

# Update One Category
@router.put("/{category_id}")
def update_one_category(product: UpdateCategory, category_id: int = Path(description="The ID of the category")):
    if category_id >= len(db_categories):
        raise HTTPException(status_code=404, detail="Category not found!")

    old_category = db_categories[category_id]
    update_category = product.dict(exclude_unset=True)
    new_category = old_category.copy(update=update_category)

    db_categories[category_id] = jsonable_encoder(new_category)

    return {"data": new_category}
