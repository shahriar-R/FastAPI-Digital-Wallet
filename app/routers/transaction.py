from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.transaction import get_transactions
from schemas.user import User
from deps import get_db
from utils.authentication import get_current_user

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/")
def get_transactions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_transactions(db=db, user=current_user)
