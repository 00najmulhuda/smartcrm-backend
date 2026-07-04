from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .blog_post import BlogPost
    from .comment import Comment
    from .lead import Lead
    from .note import Note




class User(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key = True)
    name : str = Field(index = True)
    email : str = Field(unique = True)
    hashed_password : str
    role : str = Field(default = "user")
    blog_posts : list["BlogPost"] = Relationship(back_populates="user")
    comments : list["Comment"] = Relationship(back_populates="user")
    leads : list["Lead"] = Relationship(back_populates="user")
    notes : list["Note"] = Relationship(back_populates="user")
    created_at : datetime = Field(default_factory = datetime.utcnow)


