from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Wallet as WalletModel
from app.schemas import user as UserSchema

async def deposit(db: AsyncSession, user: UserSchema.User, amount: float):
    wallet = db.execute(WalletModel.Wallet).filter(WalletModel.Wallet.owner_id == user.id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    wallet.balance += amount
    db.commit()
    db.refresh(wallet)
    return wallet
