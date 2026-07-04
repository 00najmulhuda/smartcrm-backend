from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    name : str = Field(min_length = 4, max_length = 15)
    email : EmailStr
    password : str = Field(min_length = 8, pattern = r"^[a-zA-Z0-9_]+$")
    role : str = Field(default = "user")

class UserLogin(BaseModel):
    email : EmailStr
    password : str = Field(min_length = 8, pattern = r"^[a-zA-Z0-9_]+$")

class UserRead(BaseModel):
    id : int
    name : str
    email : EmailStr
    role : str
    created_at : datetime

class UserUpdate(BaseModel):
    name : Optional[str] = Field(default=None)
    email : Optional[EmailStr] = Field(default=None)
    password : Optional[str] = Field(
        default = None,
        min_length = 8,
        pattern = r"^[a-zA-Z0-9_]+$"
    )