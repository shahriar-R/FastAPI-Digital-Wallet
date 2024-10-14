from sqlalchemy.orm import Session
from models import user as UserModel
from schemas import user as UserSchema
from utils.authentication import hash_password

def create_user(db: Session, user: UserSchema.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = UserModel.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
