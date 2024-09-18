from models.model import Gender, Review, User, Category, EnumCategories, Product
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
    Product(id=0, name="Spider-Verse Comic", description="Full art coverback", category=EnumCategories.comic_books, quantity=10, price=6.99),
    Product(id=1, name="Yu-Gi-Oh! Plunder Patroll Deck", description="Top rouge tier full playable deck", category=EnumCategories.trading_card_games, quantity=5, price=25.50),
    Product(id=2, name="Catan Board Game", category=EnumCategories.board_games, quantity=3, price=40.39)
]

# Ürünler veritabanı
db_reviews: List[Product] = [
    Review(id=0, user_id=1, product_id=2, rating=7, comment="Good to collect")
]

# Tek bir veritabanı yapısı
db = {
    "users": db_users,
    "categories": db_categories,
    "products": db_products,
    "reviews": db_reviews
}
