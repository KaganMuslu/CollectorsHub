from fastapi import FastAPI
from routers import user, category, product

app = FastAPI()

# Main
@app.get("/", tags=["Main"])
def root():
    return {"data":"Welcome to CollectorsHub!"}

# About
@app.get("/about", tags=["Main"])
def root():
    return {"data":"This API was written by Unal Kagan Muslu to connect collectors from all around the world."}


# Routers
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(category.router, prefix="/category", tags=["Categories"])
app.include_router(product.router, prefix="/product", tags=["Products"])
