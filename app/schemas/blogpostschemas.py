from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class BlogPostCreate(BaseModel):
    title : str = Field(min_length=3, max_length=100)
    content : str = Field(min_length=10, max_length=200)
    status : str = Field(default="draft")
    image_url : Optional[str]
    category_id : int

class BlogPostRead(BaseModel):
    id : int 
    title : str
    content : str
    status : str
    image_url : str | None = None
    user_id : int
    category_id : int
    created_at : datetime

class BlogPostUpdate(BaseModel):
    title : Optional[str] = Field(default=None, min_length=3, max_length=100)
    content : Optional[str] = Field(default=None, min_length=10, max_length=200)
    status : str | None = None
    image_url : str | None = None
    category_id : int | None = None




