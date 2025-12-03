from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(100))
    address = Column(String(100))
    is_registered = Column(Boolean, default=False)

    orders = relationship('Order', back_populates='customer')
    payments = relationship('Payment', back_populates='customer')
    reviews = relationship('Review', back_populates='customer')
    