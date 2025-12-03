from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PaymentBase(BaseModel):
    order_id: int
    customer_id: int
    payment_type: str
    status: str = "pending"
    price : float

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    customer_id: Optional[int] = None
    payment_type: Optional[str] = None
    status: Optional[str] = None
    price: Optional[float] = None

class Payment(PaymentBase):
    id: int
    transaction_id: str
    payment_date: datetime

    class Config:
        from_attributes = True



