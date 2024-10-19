
from sqlalchemy import Column, Integer, Float, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from . import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, ForeignKey("users.username"))
    amount = Column(Float)
    transaction_type = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="transactions")