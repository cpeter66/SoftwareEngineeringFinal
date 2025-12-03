from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), index=True, unique=True)
    promo_description = Column(String(50))
    discount = Column(DECIMAL(5,2))
    expiration_date = Column(DateTime, nullable=False)
    active = Column(Boolean, default=True)
    creation_date = Column(DateTime, default=datetime.now)

