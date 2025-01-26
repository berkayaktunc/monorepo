from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from core.ledgers.models import LedgerEntry
from core.ledgers.schemas import LedgerEntryCreate, LedgerEntryResponse, Balance
from api.ledgers.operations import APP_LEDGER_OPERATION_CONFIG
from database import get_session

router = APIRouter()

@router.get("/ledger/{owner_id}", response_model=Balance)
async def get_balance(owner_id: str, db: AsyncSession = Depends(get_session)):
    # Calculate total balance for owner
    query = select(func.sum(LedgerEntry.amount)).where(LedgerEntry.owner_id == owner_id)
    result = await db.execute(query)
    balance = result.scalar() or 0
    
    return Balance(owner_id=owner_id, amount=balance)

@router.post("/ledger", response_model=LedgerEntryResponse)
async def create_ledger_entry(
    entry: LedgerEntryCreate,
    db: AsyncSession = Depends(get_session)
):
    # Check if operation is valid
    if entry.operation not in APP_LEDGER_OPERATION_CONFIG:
        raise HTTPException(status_code=400, detail="Invalid operation")
    
    # Check for duplicate nonce
    query = select(LedgerEntry).where(LedgerEntry.nonce == entry.nonce)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Duplicate nonce")
    
    # Get operation amount
    amount = APP_LEDGER_OPERATION_CONFIG[entry.operation]
    
    # Check sufficient balance for negative operations
    if amount < 0:
        balance = await get_balance(entry.owner_id, db)
        if balance.amount + amount < 0:
            raise HTTPException(status_code=400, detail="Insufficient balance")
    
    # Create ledger entry
    db_entry = LedgerEntry(
        operation=entry.operation,
        amount=amount,
        nonce=entry.nonce,
        owner_id=entry.owner_id
    )
    
    db.add(db_entry)
    await db.commit()
    await db.refresh(db_entry)
    
    return db_entry 