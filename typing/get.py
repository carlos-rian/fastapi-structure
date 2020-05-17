
from pydantic import BaseModel

class UserType(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

class ItemType(BaseModel):
    id: int
    name: str
    title: str
    description: str
    owner_id: int