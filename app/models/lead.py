from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User
    from .note import Note

class Lead(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str = Field(index = True)
    email : str 
    phone : str 
    status : str = Field(default = "new")
    document_url : str | None = Field(nullable = True, default = None)
    user_id : int = Field(foreign_key = "user.id")
    user : "User" = Relationship(back_populates="leads")
    notes : list["Note"] = Relationship(back_populates="lead")
    created_at: datetime = Field(default_factory = datetime.utcnow)