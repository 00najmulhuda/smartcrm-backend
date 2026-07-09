from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select

from app.database import get_session
from app.dependencies import get_current_user
from app.models.note import Note
from app.models.lead import Lead
from app.schemas.noteschemas import NoteCreate, NoteRead, NoteUpdate

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

@router.get("/notes",response_model=list[NoteRead])
def get_my_notes(
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_note = session.exec(select(Note).where(Note.user_id == current_user.id)).all()

    return db_note

@router.get("/notes/{note_id}",response_model=NoteRead)
def get_note(
    note_id:int,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_note = session.get(Note,note_id)
    if not db_note:
        raise HTTPException(status_code=404,detail="note not found")

    if db_note.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="access denied")

    return db_note

@router.put("/notes/{note_id}", response_model=NoteRead)
def update_note(
    update:NoteUpdate,
    note_id:int,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_note = session.get(Note,note_id)
    if not db_note:
        raise HTTPException(status_code=404,detail="note not found")
    
    if db_note.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="access denied")

    if update.content is not None:
        db_note.content = update.content

    session.commit()
    session.refresh(db_note)

    return db_note

@router.delete("/notes/{note_id}", status_code=200)
def delete_note(
    note_id:int,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_note = session.get(Note,note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="note not found")

    if db_note.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="access denied")

    session.delete(db_note)
    session.commit()

    return {
        "message" : "note deleted successfully"
    }