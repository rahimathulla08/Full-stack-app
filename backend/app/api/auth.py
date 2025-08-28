from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..database import get_db
from ..models import User
from ..schemas import RegisterRequest, LoginRequest, Token, UserOut
from ..utils.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
async def register(payload: RegisterRequest, db: AsyncSession = Depends(get_db)):
    # Check uniqueness
    res1 = await db.execute(select(User).where(User.email == payload.email))
    if res1.scalar_one_or_none():
        raise HTTPException(400, detail="Email already registered")
    res2 = await db.execute(select(User).where(User.username == payload.username))
    if res2.scalar_one_or_none():
        raise HTTPException(400, detail="Username already taken")

    user = User(
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.post("/login", response_model=Token)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(User).where(User.email == payload.email))
    user = res.scalar_one_or_none()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(401, detail="Invalid credentials")
    token = create_access_token(str(user.id))
    return Token(access_token=token)