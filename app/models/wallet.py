from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float, default=0.0)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="wallets")
