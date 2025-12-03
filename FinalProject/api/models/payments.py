from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payments(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    payment_type = Column(String(100))
    status = Column(String(100), default='pending')
    price = Column(DECIMAL(10,2))
    transaction_id = Column(String(100), unique=True)
    payment_date = Column(DateTime, default=datetime.now)

    order = relationship('Order', backref='payments')
    customer = relationship('Customer', backref='payments')
