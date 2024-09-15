from fastapi import APIRouter, HTTPException, Path
from models.model import Product, UpdateProduct
from models.database import db_products

router = APIRouter()


# Get All Products
@router.get("")
def all_products():
    return {"data": db_products }

# Add One Product
@router.post("")
def post_product(product: Product):
    db_products.append(product)
    return {"data": "successfull!"}

# Get One Product
@router.get("/{product_id}")
def get_one_product(product_id: int = Path(description="The ID of the product") ):
    if product_id >= len(db_products):
        raise HTTPException(status_code=404, detail="Product not found!")
    
    return {"data": db_products[product_id] } 

# Delete One Product
@router.delete("/{product_id}")
def delete_one_product(product_id: int = Path(description="The ID of the product") ):
    if product_id >= len(db_products):
        raise HTTPException(status_code=404, detail="Product not found!")
    
    db_products.remove(db_products[product_id])
    return {"data": "deleted!"}

# Update One Product
@router.put("/{product_id}")
def update_one_product(product:UpdateProduct, product_id: int = Path(description="The ID of the product")):
    if product_id >= len(db_products):
        raise HTTPException(status_code=404, detail="Product not found!")

    oldProduct = db_products[product_id]
    
    if product.name is not None:
        oldProduct.name = product.name
    if product.categoty is not None:
        oldProduct.categoty = product.categoty
    if product.quantity is not None:
        oldProduct.quantity = product.quantity
    if product.price is not None:
        oldProduct.price = product.price

    return {"data": db_products[product_id] }
