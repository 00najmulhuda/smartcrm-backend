from sqlmodel import Relationship, SQLModel, Field

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .blog_post import BlogPost


class Category(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str = Field(index = True, unique = True)
    blog_posts : list["BlogPost"] = Relationship(back_populates="category")