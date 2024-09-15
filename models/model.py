from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

# Enums
class Gender(str, Enum):
    male = "male"
    female = "female"

class Categories(str, Enum):
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
    name: Categories

# Products Table
class Product(BaseModel):
    id: int
    name: str
    categoty: Categories
    quantity: int
    price: Optional[int] = None