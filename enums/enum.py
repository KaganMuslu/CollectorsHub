# Enums
from enum import Enum


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
