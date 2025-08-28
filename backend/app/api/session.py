from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from ..database import get_db
from ..models import ChatSession
from ..schemas import SessionCreate, SessionOut, SessionUpdate
from ..utils.deps import get_current_user
from ..config import settings

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.get("/", response_model=List[SessionOut])
async def list_sessions(db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    res = await db.execute(select(ChatSession).where(ChatSession.user_id == user.id).order_by(ChatSession.created_at.desc()))
    return res.scalars().all()

@router.post("/", response_model=SessionOut)
async def create_session(payload: SessionCreate, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    provider = payload.provider or settings.DEFAULT_PROVIDER
    model = payload.model or settings.DEFAULT_MODEL
    sess = ChatSession(user_id=user.id, title=payload.title, provider=provider, model=model)
    db.add(sess)
    await db.commit()
    await db.refresh(sess)
    return sess

@router.get("/{session_id}", response_model=SessionOut)
async def get_session(session_id: str, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    sess = await db.get(ChatSession, session_id)
    if not sess or sess.user_id != user.id:
        raise HTTPException(404, detail="Session not found")
    return sess

@router.patch("/{session_id}", response_model=SessionOut)
async def update_session(session_id: str, payload: SessionUpdate, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    sess = await db.get(ChatSession, session_id)
    if not sess or sess.user_id != user.id:
        raise HTTPException(404, detail="Session not found")
    if payload.title is not None:
        sess.title = payload.title
    if payload.provider is not None:
        sess.provider = payload.provider
    if payload.model is not None:
        sess.model = payload.model
    await db.commit()
    await db.refresh(sess)
    return sess

@router.delete("/{session_id}")
async def delete_session(session_id: str, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    sess = await db.get(ChatSession, session_id)
    if not sess or sess.user_id != user.id:
        raise HTTPException(404, detail="Session not found")
    await db.delete(sess)
    await db.commit()
