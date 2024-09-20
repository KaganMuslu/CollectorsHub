from typing import Optional
from pydantic import BaseModel
from enums.enum import EnumCategories, Gender

# User Pydantic Model
class PydanticUser(BaseModel):
    username: str
    password: str
    gender: Optional[Gender] = None

# Category Pydantic Model
class PydanticCategory(BaseModel):
    name: EnumCategories

# Products Table
class PydanticProduct(BaseModel):
    name: str
    description: Optional[str] = None
    category_id: int
    quantity: int
    price: Optional[float] = None

class PydanticReview(BaseModel):
    product_id: int
    user_id: int
    rating: int
    comment: Optional[str] = None


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
