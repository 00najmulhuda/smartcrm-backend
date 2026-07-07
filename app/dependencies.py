from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlmodel import Session, select 

from app.auth import verify_access_token
from app.database import get_session
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl= "/auth/login"
)


def get_current_user(
    token : str = Depends(oauth2_scheme),
    session:Session = Depends(get_session)
):
   token_data = verify_access_token(token)

   db_user = session.exec(select(User).where(User.id == token_data["user_id"])).first()
   if not db_user:
    raise HTTPException(status_code=401, detail = "token expire or wrong token")

   return db_user


def require_role(required_role : str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(status_code=403, detail= "access_denied")
        return current_user

    return role_checker
