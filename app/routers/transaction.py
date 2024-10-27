from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.transaction import get_transactions
from app.schemas.user import User
from app.deps import get_db
from app.utils.authentication import get_current_user

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/")
async def get_transactions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    result= await get_transactions(db=db, user=current_user)
    return result