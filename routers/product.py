from fastapi import APIRouter, Depends, HTTPException, Path
from models.pydantic import PydanticProduct, UpdateProduct
from models.model import Product, get_db
from sqlalchemy.orm import Session

router = APIRouter()

# If product exist returns product
def product_db_query(db, product_id):
    product = db.query(Product).filter(Product.id == product_id).first()
    if (product == None):
        raise HTTPException(status_code=404, detail="Product not found!")
    else:
        return product


# Get All Products
@router.get("")
def all_products(limit: int = 10, skip: int = 0, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return {"data": products}


# Add One Product
@router.post("", status_code=201)
def post_product(product: PydanticProduct, db: Session = Depends(get_db)):
    new_product = Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    return {"data": "successfull!"}

# Get One Product
@router.get("/{product_id}")
def get_one_product(product_id: int = Path(description="The ID of the product"), db: Session = Depends(get_db)):
    product = product_db_query(db, product_id)
    
    return {"data": product} 

# Delete One Product
@router.delete("/{product_id}")
def delete_one_product(product_id: int = Path(description="The ID of the product"), db: Session = Depends(get_db)):
    product = product_db_query(db, product_id)
    db.delete(product)
    db.commit()
    
    return {"data": "deleted!"}

# Update One Product
@router.put("/{product_id}")
def update_one_product(product: UpdateProduct, product_id: int = Path(description="The ID of the product"), db: Session = Depends(get_db)):
    old_product = product_db_query(db, product_id)

    update_data = product.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(old_product, key, value)

    db.commit()
    new_product = db.query(Product).filter(Product.id == product_id).first()

    return {"data": new_product}
