from fastapi import FastAPI
from sqlalchemy import Select
from models import MenuItem, CategoryType, CuisineType
from routes import route

app = FastAPI()
app.include_router(route.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
