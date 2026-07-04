from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class CommentCreate(BaseModel):
    content : str = Field(min_length=1, max_length=20)
    blog_post_id : int


class CommentRead(BaseModel):
    id : int
    content : str
    user_id : int 
    blog_post_id : int
    created_at : datetime

class CommentUpdate(BaseModel):
    content : Optional[str] = Field(default=None)

