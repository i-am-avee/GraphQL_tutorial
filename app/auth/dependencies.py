from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth.auth import decode_token
from app.db.user_entity import UserEntity  # Adjust import based on your structure
from app.types.user_type import UserType
from app.db.database import SessionLocal


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str) -> UserType:
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload["sub"]

    # Fetch user from DB
    db = SessionLocal()
    user = db.query(UserEntity).filter(UserEntity.id == user_id).first()
    db.close()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user