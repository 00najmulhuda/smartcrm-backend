from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .category import Category
    from .user import User
    from .comment import Comment

class BlogPost(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    title : str = Field(index = True)
    content : str 
    user_id : int = Field(foreign_key = "user.id")
    category_id : int = Field(foreign_key = "category.id")
    image_url : str | None = Field(nullable = True, default = None)
    status : str = Field(default = "draft")
    user : "User" = Relationship(back_populates="blog_posts")
    category : "Category" = Relationship(back_populates="blog_posts")
    comments : list["Comment"] = Relationship(back_populates="blog_post")
    created_at : datetime = Field(default_factory = datetime.utcnow)