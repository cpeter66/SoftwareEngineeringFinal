from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    track_num = Column(String(50), unique=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_time = Column(DateTime, default=datetime.now)
    order_status = Column(String(50), default='pending')
    total = Column(DECIMAL(10,2))
    order_type = Column(String(50), default='Delivery')
    address_for_delivery = Column(String(50))