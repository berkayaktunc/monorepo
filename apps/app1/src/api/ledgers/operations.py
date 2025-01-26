from core.ledgers.operations import create_ledger_operation, LEDGER_OPERATION_CONFIG

AppLedgerOperation = create_ledger_operation(
    "AppLedgerOperation",
    {
        "CONTENT_CREATION": "CONTENT_CREATION",
        "CONTENT_ACCESS": "CONTENT_ACCESS"
    }
)

APP_LEDGER_OPERATION_CONFIG = {
    **LEDGER_OPERATION_CONFIG,
    "CONTENT_CREATION": -5,
    "CONTENT_ACCESS": 0,
} 