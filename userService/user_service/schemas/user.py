from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    #so basically we've got a base user model 
    #simply stotring username here cz thats like unique
    userName: str = Field(..., min_length=3, max_length=50)

class UserCreate(UserBase):
    #extends userbase class and inherits the username 
    password: str = Field(..., min_length=4)

class UserInDB(UserBase): 
    #id is auto increment
    id: int
    created_at: datetime

    class Config:
        from_attributes = True 
        #this true makes sure that sqlalchemy orm is enables

class UserResponse(UserInDB):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel): 
    username: Optional[str] = None