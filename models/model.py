from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enums.enum import EnumCategories, Gender


# Users Table
class User(BaseModel):
    id: int
    username: str
    password: str
    gender: Gender

# Categories Table
class Category(BaseModel):
    id: int
    name: EnumCategories

# Products Table
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    category: EnumCategories
    quantity: int
    price: Optional[float] = None

class Review(BaseModel):
    id: int
    user_id: int
    product_id: int
    rating: int
    comment: Optional[str] = None
    review_date: datetime = datetime.now()



### UPDATE MODELS

# User Update Model
class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    gender: Optional[Gender] = None

# Category Update Model
class UpdateCategory(BaseModel):
    name: Optional[EnumCategories] = None

# Products Table
class UpdateProduct(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[EnumCategories] = None
    quantity: Optional[int] = None
    price: Optional[float] = None

class UpdateReview(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None
    review_date: datetime = datetime.now()
