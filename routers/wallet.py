from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.wallet import deposit
from schemas.user import User
from deps import get_db
from utils.authentication import get_current_user

router = APIRouter(
    prefix="/wallet",
    tags=["wallet"]
)

@router.post("/deposit/")
def deposit(amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return deposit(db=db, user=current_user, amount=amount)
