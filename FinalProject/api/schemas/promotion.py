from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class PromotionBase(BaseModel):
    code: str
    promo_description: str
    discount: float
    expiration_date: datetime
    active: bool = True
class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    promo_description: Optional[str] = None
    discount: Optional[float] = None
    expiration_date: Optional[datetime] = None
    active: Optional[bool] = None

class Promotion(PromotionBase):
    id: int
    creation_date: datetime

    class Config:
        from_attributes = True
