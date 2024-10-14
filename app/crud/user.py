from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models import user as UserModel
from utils.authentication import hash_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()

def create_user(db: Session, username: str, password: str):
    hashed_password = hash_password(user.password)
    db_user = UserModel.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)