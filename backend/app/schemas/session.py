from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class SessionCreate(BaseModel):
    title: Optional[str] = None
    provider: Optional[str] = None
    model: Optional[str] = None

class SessionUpdate(BaseModel):
    title: Optional[str] = None
    provider: Optional[str] = None
    model: Optional[str] = None

class SessionOut(BaseModel):
    id: UUID
    title: Optional[str]
    provider: Optional[str]
    model: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
