from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Transaction as TransactionModel
from app.schemas import user as UserSchema

async def get_transactions(db: AsyncSession, user: UserSchema.User):
    result = await db.execute(TransactionModel.Transaction).filter(models.Transaction.username == user.username).all()
    return result