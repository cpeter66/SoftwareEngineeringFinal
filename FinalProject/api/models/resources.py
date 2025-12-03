from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from ..schemas import resource


class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    ingredient = Column(String(100), nullable=False)
    quantity = Column(DECIMAL(10,2), nullable=False)
    unit_measure = Column(String(20), nullable=False)

    menu_item = relationship('MenuItem', back_populates="resources")