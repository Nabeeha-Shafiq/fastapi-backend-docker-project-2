from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    userName: str = Field(..., min_length=3, max_length=50)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserInDB(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True 
        #tells pydantic to read data from SQLAlchemy models

class UserResponse(UserInDB):
    pass