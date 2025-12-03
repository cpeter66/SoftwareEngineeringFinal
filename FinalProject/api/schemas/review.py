from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ReviewBase(BaseModel):
    order_id: int
    customer_id: int
    rating: int
    review_text: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    order_id: Optional[int] = None
    customer_id: Optional[int] = None
    rating: Optional[int] = None
    review_text: Optional[str] = None

class Review(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
