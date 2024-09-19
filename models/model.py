from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enums.enum import EnumCategories, Gender

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, create_engine, Enum, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY CONNECTION
engine = create_engine("sqlite:///CollectorsHub.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(engine)
Base = declarative_base()


# Users Table
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    gender = Column(Enum(Gender), nullable= True)

    products = relationship("Product", back_populates="user")
    reviews = relationship("Review", back_populates="user")

# Categories Table
class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(EnumCategories))

    products = relationship("Product", back_populates="category")

# Products Table
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    quantity = Column(Integer)
    price = Column(Float, nullable=True)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="products")
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="products")
    reviews = relationship("Review", back_populates="product")

# Reviews Table
class Review(Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    comment = Column(String, nullable=True)
    review_date = Column(DateTime, default=func.now)

    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("Product", back_populates="reviews")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="reviews")

# Create every model
Base.metadata.create_all(engine)

# DB Connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


### PYDANTIC MODELS

# User Pydantic Model
class PydanticUser(BaseModel):
    username: str
    password: str
    gender: Optional[Gender] = None

# Category Pydantic Model
class PydanticCategory(BaseModel):
    name: Optional[EnumCategories] = None

# Products Table
class PydanticProduct(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[EnumCategories] = None
    quantity: Optional[int] = None
    price: Optional[float] = None

class PydanticReview(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None
    review_date: Optional[datetime] = datetime.now()


### PYDANTIC UPDATE MODELS

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
    review_date: Optional[datetime] = datetime.now()






### TÜM PDATE OLMAYAN PYTDANTIC MODELLERİ DÜZENLE