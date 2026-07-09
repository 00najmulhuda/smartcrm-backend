from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class LeadCreate(BaseModel):
    name : str = Field(min_length=3, max_length=15)
    email : EmailStr
    phone : str = Field(pattern=r"^\+?[0-9]{10,15}$")
    status : str = Field(default="new")
    document_url : Optional[str] = Field(default=None)

class LeadRead(BaseModel):
    id : int
    name : str
    email : EmailStr
    phone : str
    status : str
    document_url : str | None = None
    user_id : int
    created_at : datetime

class LeadUpdate(BaseModel):
    name : Optional[str] = Field(default=None, min_length=3, max_length=15)
    email : Optional[EmailStr] = Field(default = None)
    phone : Optional[str] = Field(default=None, pattern=r"^\+?[0-9]{10,15}$")
    status : Optional[str] = Field(default=None)
    document_url : Optional[str] = Field(default=None)



