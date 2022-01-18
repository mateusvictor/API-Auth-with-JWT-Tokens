from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = True


class UserCreate(UserBase):
	password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str