from datetime import datetime
from typing import Optional
from sqlalchemy import Integer, String, DateTime, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .operations import SharedLedgerOperation

class Base(DeclarativeBase):
    pass

class LedgerEntry(Base):
    __tablename__ = "ledger_entries"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    operation: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    nonce: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    owner_id: Mapped[str] = mapped_column(String, nullable=False)
    created_on: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    ) 