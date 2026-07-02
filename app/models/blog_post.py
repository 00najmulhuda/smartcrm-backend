from sqlmodel import SQLModel, Field
from datetime import datetime

class BlogPost(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    title : str = Field(index = True)
    content : str 
    user_id : int = Field(foreign_key = "user.id")
    category_id : int = Field(foreign_key = "category.id")
    image_url : str |None = Field(nullable = True)
    status : str = Field(default = "draft")
    created_at : datetime = Field(default_factory = datetime.utcnow)