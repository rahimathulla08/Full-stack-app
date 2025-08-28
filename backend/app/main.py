# main.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .database import engine, Base, get_db
from .models import ChatSession, Message


# -------------------------------
# Pydantic Models
# -------------------------------
class ChatRequest(BaseModel):
    session_id: int
    message: str


# -------------------------------
# Lifespan Events
# -------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("✅ App is starting up")
    async with engine.begin() as conn:
        # Create all tables if not exists
        await conn.run_sync(Base.metadata.create_all)
    yield
    print("🛑 App is shutting down")


# -------------------------------
# App Initialization
# -------------------------------
app = FastAPI(lifespan=lifespan)

# Enable CORS for frontend (React runs on localhost:3000 by default)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # update if frontend runs elsewhere
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------
# API Routes
# -------------------------------

# ✅ Create new chat session
@app.post("/session")
async def create_session(db: AsyncSession = Depends(get_db)):
    new_session = ChatSession(name="New Chat")
    db.add(new_session)
    await db.commit()
    await db.refresh(new_session)
    return {"id": new_session.id, "name": new_session.name}


# ✅ Chat endpoint (send/receive messages)
@app.post("/api/Chat")
async def chat(request: ChatRequest, db: AsyncSession = Depends(get_db)):
    # Save user message
    user_msg = Message(
        session_id=request.session_id,
        role="user",
        content=request.message,
    )
    db.add(user_msg)

    # Generate dummy AI reply (replace with actual model later)
    ai_reply = f"AI reply to: {request.message}"

    # Save AI message
    ai_msg = Message(
        session_id=request.session_id,
        role="ai",
        content=ai_reply,
    )
    db.add(ai_msg)

    await db.commit()
    await db.refresh(ai_msg)

    return {"reply": ai_reply}


# ✅ Get all messages from a chat session
@app.get("/sessions/{session_id}/messages")
async def get_messages(session_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Message).where(Message.session_id == session_id).order_by(Message.id)
    )
    messages = result.scalars().all()
    return [
        {"id": m.id, "role": m.role, "content": m.content}
        for m in messages
    ]
