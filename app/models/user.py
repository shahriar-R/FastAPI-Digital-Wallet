from sqlalchemy import  Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)

    wallets: Mapped[list["Wallet"]] = relationship("Wallet", back_populates="owner")
    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="user")