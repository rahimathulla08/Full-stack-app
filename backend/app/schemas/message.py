from pydantic import BaseModel
from typing import Optional, Any
from uuid import UUID
from datetime import datetime

class MessageCreate(BaseModel):
    content: str

class MessageOut(BaseModel):
    id: UUID
    session_id: UUID
    role: str
    content: str
    provider: Optional[str]
    model: Optional[str]
    tokens_used: int
    created_at: datetime
    metadata: Any

    class Config:
        from_attributes = True