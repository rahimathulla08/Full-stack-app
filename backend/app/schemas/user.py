from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserOut(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True