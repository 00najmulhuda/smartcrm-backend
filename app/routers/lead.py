from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.sql.functions import current_user
from sqlmodel import SQLModel, Session,select

from app.database import get_session
from app.dependencies import get_current_user
from app.models.lead import Lead
from app.schemas.leadschemas import LeadCreate, LeadRead



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