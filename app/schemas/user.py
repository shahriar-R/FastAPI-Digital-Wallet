from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    
class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserResponse(User):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True