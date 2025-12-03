from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OrderBase(BaseModel):
    customer_id: Optional[int] = None
    total: float
    order_status: str = "pending"
    order_type: str = "Delivery"
    address_for_delivery: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    total: Optional[float] = None
    order_status: Optional[str] = None
    order_type: Optional[str] = None
    address_for_delivery: Optional[str] = None

class Order(OrderBase):
    id: int
    track_num: str
    order_time: datetime

    class Config:
        from_attributes = True

