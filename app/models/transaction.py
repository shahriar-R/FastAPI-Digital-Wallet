from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.sql import func
from ..database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, ForeignKey("users.username"))
    amount = Column(Float)
    transaction_type = Column(String)
    timestamp = Column(func.now())
