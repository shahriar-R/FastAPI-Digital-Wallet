from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud.user import get_user, create_user, verify_password
from schemas.user import UserLogin, UserCreate
from deps import get_db
from utils.authentication import create_access_token, verify_password
from datetime import timedelta

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user.username, user.password)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user(db, username=user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
