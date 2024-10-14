from pydantic import BaseModel

class TransactionBase(BaseModel):
    amount: float
    transaction_type: str

class Transaction(TransactionBase):
    id: int
    username: str

    class Config:
        orm_mode = True
