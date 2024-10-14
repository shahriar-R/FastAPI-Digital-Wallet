from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models.user import User as modelUser
from utils.authentication import hash_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, username: str):
    return db.query(modelUser).filter(modelUser.username == username).first()

def create_user(db: Session, username: str, password: str, email:str):
    hashed_password = hash_password(password)
    db_user = modelUser(username=username, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)