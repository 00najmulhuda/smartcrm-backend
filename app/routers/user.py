from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select

from app.database import get_session
from app.dependencies import get_current_user
from app.auth import hash_password
from app.models.user import User
from app.schemas.userschemas import UserRead, UserUpdate


router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/users/me",response_model=UserRead)
def get_me(
    current_user = Depends(get_current_user)
):
    return current_user

@router.put("/user/me",response_model=UserRead)
def update_user(
    update:UserUpdate,
    session:Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_user = session.get(User, current_user.id)
    if not db_user:
        raise HTTPException(status_code=404,detail="user not found")

    if db_user.id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="access denied")

    if update.name is not None:
        db_user.name = update.name

    if update.email is not None:
        check_existing = session.exec(
            select(User)
            .where(User.email == update.email)
        ).first()
        if check_existing and check_existing.id == current_user.id:
            raise HTTPException(status_code=409, detail="already exist")
        else:
            db_user.email = update.email

    if update.password is not None:
        db_user.hashed_password =hash_password(update.password)

    session.commit()
    session.refresh(db_user)

    return db_user