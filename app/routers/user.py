from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.user import get_user, create_user, verify_password, get_all_user
from app.schemas.user import UserLogin, UserCreate, UserResponse
from app.deps import get_db
from app.utils.authentication import create_access_token, verify_password, get_current_user
from datetime import timedelta

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/register/")
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
   
    await create_user(db, user.username, user.password, user.email)
    return {"message": "User registered successfully"}


@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db, username=user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/current-user", response_model=UserResponse)
async def current_user(user: UserResponse = Depends(get_current_user)):
    return user

@router.get("/all-user")
async def user(user:UserResponse, db: AsyncSession= Depends(get_db)):
    return get_all_user(db=db)