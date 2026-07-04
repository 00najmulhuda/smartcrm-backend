from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class CategoryCreate(BaseModel):
    name : str = Field(min_length = 3, max_length = 50)

class CategoryRead(BaseModel):
    id : int
    name : str

class CategoryUpdate(BaseModel):
    name : Optional[str] = Field(default=None, min_length=3, max_length=50)