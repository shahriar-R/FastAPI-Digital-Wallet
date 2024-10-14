from sqlalchemy.orm import Session
from models import transaction as TransactionModel
from schemas import user as UserSchema

def get_transactions(db: Session, user: UserSchema.User):
    return db.query(TransactionModel.Transaction).filter(models.Transaction.username == user.username).all()
