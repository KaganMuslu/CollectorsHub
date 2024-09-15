from fastapi import FastAPI
from routers import user, category, product

app = FastAPI()

# Main Point
@app.get("/", tags=["Main Point"])
def root():
    return {"data":"hello great api!"}

# Routers
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(category.router, prefix="/category", tags=["Categories"])
app.include_router(product.router, prefix="/product", tags=["Products"])
