from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database import SessionLocal
import schemas
import crud

router = APIRouter(
    prefix="/menu_items"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.MenuItemModel])
def get_menu_items(db: Session = Depends(get_db)):
    menu_items = crud.get_menu_items(db)
    return menu_items