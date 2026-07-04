from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select 
from app.auth import hash_password
from app.models.user import User
from app.database import get_session
from app.schemas.userschemas import UserRead,UserCreate



router = APIRouter(
    prefix="/auth",
    tags = ["Authentication"]
)

@router.post("/register", response_model=UserRead)
def create_user(user:UserCreate, session:Session = Depends(get_session)):
    check_email = session.exec(
        select(User)
        .where(User.email == user.email)
    ).first()
    if check_email:
        raise HTTPException(status_code=409, detail="email already exist")
    hashed_pw = hash_password(user.password)

    db_user = User(
        name = user.name,
        email = user.email,
        hashed_password= hashed_pw,
        role = "user"

    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user