from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select 
from app.auth import hash_password,verify_password,create_access_token,verify_access_token
from app.models.user import User
from app.database import get_session
from app.schemas.userschemas import UserRead,UserCreate
from fastapi.security import OAuth2PasswordRequestForm

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


@router.post("/login")
def login_user(form_data : OAuth2PasswordRequestForm = Depends(), session:Session = Depends(get_session)):
    check_email = session.exec(select(User).where(User.email == form_data.username)).first()
    if not check_email:
        raise HTTPException(status_code=401, detail= "email or password wrong")

    if not verify_password(
        form_data.password,
        check_email.hashed_password
    ):
       raise HTTPException(status_code=401, detail= "email or password wrong")

    access_token = create_access_token(
        {
            "sub" : str(check_email.id),
            "role": check_email.role
        }
    )
    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }



