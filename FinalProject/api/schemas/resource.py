from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ResourceBase(BaseModel):
    menu_item_id: int
    ingredient : str
    quantity : float
    unit_measure : str

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    ingredient: Optional[str] = None
    quantity: Optional[float] = None
    unit_measure: Optional[str] = None

class Resource(ResourceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

