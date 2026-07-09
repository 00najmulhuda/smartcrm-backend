from turtle import getscreen
from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select

from app.database import get_session
from app.dependencies import get_current_user, require_role
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

@router.get("/users",response_model=list[UserRead])
def get_all_users(
    session:Session = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    db_users = session.exec(
        select(User)
    ).all()

    return db_users

@router.get("/users/{user_id}", response_model=UserRead)
def get_user(
    user_id:int,
    session:Session = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    db_user = session.get(User,user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")

    return db_user

@router.delete("/users/{user_id}", status_code=200)
def delete_user(
    user_id:int,
    session:Session=Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    db_user = session.get(User,user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")

    if db_user.id == current_user.id:
        raise HTTPException(status_code=400, detail= "you can not delete yourself")

    session.delete(db_user)
    session.commit()

    return {
        "message" : "user deleted successfully"
    }