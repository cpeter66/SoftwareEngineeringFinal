from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    calories: Optional[int] = None
    category: Optional[str] = None
    available: bool = True


class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    category: Optional[str] = None
    available: Optional[bool] = True

class MenuItem(MenuItemBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
