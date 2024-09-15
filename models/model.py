from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

# Enums
class Gender(str, Enum):
    male = "male"
    female = "female"

class EnumCategories(str, Enum):
    comic_books = "Comic Books"
    trading_card_games = "Trading Card Games"
    board_games = "Board Games"
    figures_and_statues = "Figures and Statues"
    books_and_novels = "Books and Novels"
    gaming_collectibles = "Gaming Collectibles"


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
    category: EnumCategories
    quantity: int
    price: Optional[int] = None

    class Config:
        use_enum_values = False 


# User Update Model
class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    gender: Optional[Gender] = None

# Category Update Model
class UpdateCategory(BaseModel):
    name: Optional[EnumCategories] = None

# Product Update Model
class UpdateProduct(BaseModel):
    name: Optional[str] = None
    categoty: Optional[EnumCategories] = None
    quantity: Optional[int] = None
    price: Optional[int] = None