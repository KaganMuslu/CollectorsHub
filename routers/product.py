from fastapi import APIRouter, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from models.model import Product, UpdateProduct
from models.database import db

router = APIRouter()


# Get All Products
@router.get("")
def all_products():
    return {"data": db["products"] }

# Add One Product
@router.post("", status_code=201)
def post_product(product: Product):
    db["products"].append(product)
    return {"data": "successfull!"}

# Get One Product
@router.get("/{product_id}")
def get_one_product(product_id: int = Path(description="The ID of the product") ):
    if product_id >= len(db["products"]):
        raise HTTPException(status_code=404, detail="Product not found!")
    
    return {"data": db["products"][product_id] } 

# Delete One Product
@router.delete("/{product_id}")
def delete_one_product(product_id: int = Path(description="The ID of the product") ):
    if product_id >= len(db["products"]):
        raise HTTPException(status_code=404, detail="Product not found!")
    
    db["products"].remove(db["products"][product_id])
    return {"data": "deleted!"}

# Update One Product
@router.put("/{product_id}")
def update_one_product(product: UpdateProduct, product_id: int = Path(description="The ID of the product")):
    if product_id >= len(db["products"]):
        raise HTTPException(status_code=404, detail="Product not found!")

    old_product = db["products"][product_id]
    update_product = product.dict(exclude_unset=True)
    new_product = old_product.copy(update=update_product)

    db["products"][product_id] = jsonable_encoder(new_product)

    return {"data": new_product}
