from pydantic import BaseModel

class WalletBase(BaseModel):
    balance: float

class WalletCreate(WalletBase):
    pass

class Wallet(WalletBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
