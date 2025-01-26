from fastapi import FastAPI
from api.ledgers.router import router as ledger_router

app = FastAPI()

app.include_router(ledger_router, tags=["ledger"]) 