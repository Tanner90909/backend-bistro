from schemas import MenuItemModel
from sqlalchemy.orm import Session, aliased, joinedload
from models import MenuItem

def get_menu_items(db:Session):
    menu_items_query = (
        db.query(MenuItem).all()
    )

    return menu_items_query