from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer, Column, Float

class Base (DeclarativeBase):
    pass

class CategoryType(Base):
    __tablename__ = "category_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(String, default="Name")
    #category = relationship("MenuItem")

class CuisineType(Base):
    __tablename__ = "cuisine_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(String, default="Name")
   #cuisine = relationship("MenuItem")

class MenuItem(Base):
    __tablename__ = "menu_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")
    description: Mapped[str] = Column(String, default="Description")
    price: Mapped[float] = Column(Float, default="Price")
    spice_level: Mapped[int] = Column(Integer, default="Spice Level")
    category_type_id = Column(Integer, ForeignKey("category_types.id"))
    cuisine_type_id = Column(Integer, ForeignKey("cuisine_types.id"))

    categories = relationship("CategoryType")
    cuisines = relationship("CuisineType")

    def __repr__(self) -> str:
        return f"""MenuItem(id={self.id!r},
        name={self.name!r},
        description={self.description!r},
        price={self.price!r},
        spice_level={self.spice_level!r})
        """