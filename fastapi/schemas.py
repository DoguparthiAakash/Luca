from pydantic import BaseModel
from typing import Optional

class ItemSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class UserSchema(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
