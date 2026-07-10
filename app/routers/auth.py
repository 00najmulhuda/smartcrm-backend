import email
from token import tok_name
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select 
from app.auth import hash_password,verify_password,create_access_token,verify_access_token
from app.models.user import User
from app.database import get_session
from app.schemas.userschemas import UserRead,UserCreate
from fastapi.security import OAuth2PasswordRequestForm
from app.services.email_utils import send_email

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
    send_email(
        to_email = db_user.email,
        subject = "Welcome to Najmul Huda Blog_CRM project",
        body = f"""
Hello {db_user.name},

Your account has been created successfully.

Welcome to Najmul Blog CRM Project.

Happy Coding!

Regards,
Najmul
"""

    )
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

    send_email(
        to_email=check_email.email,
        subject="Login Alert - Najmul Blog CRM Project",
        body=f"""
Hello {check_email.name},
Your account was successfully logged in.

If this was you, no action is required.

If you did not log in, please change your password immediately.

Regards,
Najmul
        """
    )

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }



