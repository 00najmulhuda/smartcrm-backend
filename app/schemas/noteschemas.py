from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class NoteCreate(BaseModel):
    content : str = Field(min_length=2, max_length=50)
    lead_id : int


class NoteRead(BaseModel):
    id : int
    content : str
    lead_id : int
    user_id : int
    created_at : datetime

class NoteUpdate(BaseModel):
    content : Optional[str] = Field(default=None, min_length=2, max_length=50 )

