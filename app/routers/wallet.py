from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.wallet import deposit
from app.schemas.user import User
from app.deps import get_db
from app.utils.authentication import get_current_user

router = APIRouter(
    prefix="/wallet",
    tags=["wallet"]
)

@router.post("/deposit/")
async def deposit(amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_user())):
    result = await deposit(db=db, user=current_user, amount=amount)
    return result