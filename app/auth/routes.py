from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db.user_entity import UserEntity
from app.auth.auth import verify_password, create_access_token
from app.db.database import SessionLocal

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    with SessionLocal() as db:
        user = db.query(UserEntity).filter(UserEntity.email == data.username).first()
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token, "token_type": "bearer"}
