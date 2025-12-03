from sqlalchemy import Column, Integer, String, DECIMAL, Text, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String(300))
    price = Column(DECIMAL(10,2), nullable=False)
    calories = Column(Integer)
    category = Column(String(50))
    available = Column(Boolean, default=True)

    order_items = relationship('OrderItem', back_populates='menu_item')
    resources = relationship('Resource', back_populates='menu_item')