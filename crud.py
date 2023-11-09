from schemas import MenuItemModel
from sqlalchemy.orm import Session, aliased, joinedload
from models import MenuItem, CategoryType, CuisineType

def get_menu_items(db:Session):
    menu_items_query = (
        db.query(MenuItem).all()
    )

    return menu_items_query

# def get_category_and_cuisine_type(db:Session):
#     menu_items_with_category_and_cuisine_query = (
#         db.query(MenuItem).join(MenuItem.categories).join(MenuItem.cuisines).all()
#     )

def get_category_and_cuisine_type(db:Session):
    menu_items_with_category_and_cuisine_query = (
        db.query(MenuItem).options(joinedload(MenuItem.categories)).all()
    )
    
    return menu_items_with_category_and_cuisine_query