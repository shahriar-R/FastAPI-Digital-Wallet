from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.user import create_user
from schemas.user import UserCreate
from deps import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
