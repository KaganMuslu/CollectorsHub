from models.model import Gender, User, Category, EnumCategories, Product
from typing import List


# Kullanıcılar veritabanı
db_users: List[User] = [
    User(id=0, username="DualPatroll", password="asdqwe", gender=Gender.female),
    User(id=1, username="NinjaSaizo", password="jutsu21", gender=Gender.male)
]

# Kategoriler veritabanı
db_categories: List[Category] = [
    Category(id=0, name=EnumCategories.comic_books),
    Category(id=1, name=EnumCategories.trading_card_games),
    Category(id=2, name=EnumCategories.board_games)
]

# Ürünler veritabanı
db_products: List[Product] = [
    Product(id=0, name="Spider-Verse Comic", category=EnumCategories.comic_books, quantity=10, price=6.99),
    Product(id=1, name="Yu-Gi-Oh! Plunder Patroll Deck", category=EnumCategories.trading_card_games, quantity=5, price=25.50),
    Product(id=2, name="Catan Board Game", category=EnumCategories.board_games, quantity=3, price=40.39)
]

# Tek bir veritabanı yapısı
db = {
    "users": db_users,
    "categories": db_categories,
    "products": db_products
}
