from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .lead import Lead
    from .user import User



class Note(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    content : str
    lead_id : int = Field(foreign_key="lead.id")
    user_id : int = Field(foreign_key="user.id")
    lead : "Lead" = Relationship(back_populates="notes")
    user : "User" = Relationship(back_populates="notes")
    created_at : datetime = Field(default_factory= datetime.utcnow)
