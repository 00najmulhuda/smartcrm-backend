from signal import raise_signal
from fastapi import APIRouter, Depends, HTTPException
from pydantic import PastDate
from sqlalchemy.sql.functions import current_user
from sqlmodel import SQLModel, Session,select

from app.database import get_session
from app.dependencies import get_current_user
from app.models.lead import Lead
from app.schemas.leadschemas import LeadCreate, LeadRead, LeadUpdate 



router = APIRouter(
    prefix="/lead",
    tags=["Lead"]
)

@router.post("/leads",response_model=LeadRead)
def create_lead(
    lead:LeadCreate,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_lead = Lead(
        name = lead.name,
        email = lead.email,
        phone = lead.phone,
        status=lead.status,
        document_url= lead.document_url,
        user_id=current_user.id
    )

    session.add(db_lead)
    session.commit()
    session.refresh(db_lead)

    return db_lead

@router.get("/leads", response_model=list[LeadRead])
def get_my_leads(
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_leads = session.exec(
        select(Lead)
        .where(Lead.user_id == current_user.id)
    ).all()

    return db_leads

@router.get("/leads/{lead_id}", response_model=LeadRead)
def get_my_lead(
    lead_id:int,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_lead = session.get(Lead,lead_id)
    if not db_lead:
        raise HTTPException(
            status_code=404, detail="lead not found"
        )
    if db_lead.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="access denied")
    return db_lead
    
@router.put("/leads/{lead_id}", response_model=LeadRead)
def update_lead(
    update:LeadUpdate,
    lead_id:int,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_lead = session.get(Lead, lead_id)
    if not db_lead:
        raise HTTPException(
            status_code=404,
            detail="lead not found"
        )
    if db_lead.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="access denied")

    if update.name is not None:
        db_lead.name = update.name
    
    if update.email is not None:
        db_lead.email = update.email

    if update.phone is not None:
        db_lead.phone = update.phone

    if update.status is not None:
        db_lead.status = update.status

    if update.document_url is not None:
        db_lead.document_url = update.document_url

    session.commit()
    session.refresh(db_lead)

    return db_lead