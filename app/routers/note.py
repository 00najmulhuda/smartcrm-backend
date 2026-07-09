from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.sql.functions import current_date
from sqlmodel import Session,select

from app.database import get_session
from app.dependencies import get_current_user
from app.models.note import Note
from app.models.lead import Lead
from app.schemas.noteschemas import NoteCreate, NoteRead

router = APIRouter(
    prefix="/note",
    tags=["Note"]
)

@router.post("/notes",response_model=NoteRead)
def create_note(
    note:NoteCreate,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_lead = session.get(Lead, note.lead_id)
    if not db_lead:
        raise HTTPException(status_code=404,detail="lead not found")

    if db_lead.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="access denied")

    db_note = Note(
        content=note.content,
        lead_id=note.lead_id,
        user_id=current_user.id
    )

    session.add(db_note)
    session.commit()
    session.refresh(db_note)

    return db_note