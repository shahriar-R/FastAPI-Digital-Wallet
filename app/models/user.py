from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    wallets = relationship("Wallet", back_populates="owner")
    transactions = relationship("Transaction", back_populates="user")
