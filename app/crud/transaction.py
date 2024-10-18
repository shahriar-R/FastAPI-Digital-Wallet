from sqlalchemy.ext.asyncio import AsyncSession
from models import transaction as TransactionModel
from schemas import user as UserSchema

async def get_transactions(db: AsyncSession, user: UserSchema.User):
    result = await db.query(TransactionModel.Transaction).filter(models.Transaction.username == user.username).all()
    return result