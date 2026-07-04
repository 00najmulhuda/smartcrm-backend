from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .blog_post import BlogPost
    from .user import User

class Comment(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    content : str
    user_id : int = Field(foreign_key = "user.id")
    blog_post_id : int = Field(foreign_key = "blogpost.id")
    user : "User" = Relationship(back_populates="comments")
    blog_post : "BlogPost" = Relationship(back_populates="comments")
    created_at : datetime = Field(default_factory = datetime.utcnow)