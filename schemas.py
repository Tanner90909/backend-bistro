from typing import Optional
from pydantic import BaseModel

class CategoryTypeModel(BaseModel):
    id: int
    name: str | None

class CuisineTypeModel(BaseModel):
    id: int
    name: str | None

class MenuItemModel(BaseModel):
    id: int
    name: str | None
    description: str | None
    price: float | None
    spice_level: int | None