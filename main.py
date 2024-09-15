from fastapi import FastAPI
from routers import user

app = FastAPI()

# Main Point
@app.get("/", tags=["Main Point"])
def root():
    return {"data":"hello great api!"}

# Routers
app.include_router(user.router, prefix="/user", tags=["Users"])