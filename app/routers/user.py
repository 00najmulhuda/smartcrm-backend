from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select

from app.dependencies import get_current_user
from app.schemas.userschemas import UserRead


router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/users/me",response_model=UserRead)
def get_me(
    current_user = Depends(get_current_user)
):
    return current_user