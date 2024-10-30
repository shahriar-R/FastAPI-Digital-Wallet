from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from sqlalchemy.future import select

from app.models import User as modelUser
from app.utils.authentication import hash_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user(db: AsyncSession, username: str):
    query = select(modelUser).filter(modelUser.username == username)
    result = await db.execute(query)
    return result.scalars().first()

async def get_all_user(db: AsyncSession):
    query = select(modelUser).all
    result = await db.execute(query)
    return result.scalars().first()


async def create_user(db: AsyncSession, username: str, password: str, email:str):
    hashed_password = hash_password(password)
    db_user = modelUser(username=username, email=email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)