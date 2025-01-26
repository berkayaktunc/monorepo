from datetime import datetime
from pydantic import BaseModel, Field

class LedgerEntryBase(BaseModel):
    operation: str
    amount: int
    owner_id: str
    nonce: str

class LedgerEntryCreate(LedgerEntryBase):
    pass

class LedgerEntryResponse(LedgerEntryBase):
    id: int
    created_on: datetime

    class Config:
        from_attributes = True

class Balance(BaseModel):
    owner_id: str
    amount: int = Field(ge=0) 