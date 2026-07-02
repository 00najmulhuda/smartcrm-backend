from sqlmodel import SQLModel, Field
from datetime import datetime

class Comment(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    content : str
    user_id : int = Field(foreign_key = "user.id")
    blog_post_id : int = Field(foreign_key = "blogpost.id")
    created_at : datetime = Field(default_factory = datetime.utcnow)