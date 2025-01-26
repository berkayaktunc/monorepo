from enum import Enum
from typing import Dict, Type

class BaseLedgerOperation:
    """Base class for ledger operations that enforces shared operations"""
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # Enforce shared operations
        return (
            all(
                operation in subclass.__members__ 
                for operation in SharedLedgerOperation.__members__
            )
            and NotImplemented
        )

class SharedLedgerOperation(Enum):
    """Core shared ledger operations that must be implemented by all apps"""
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT" 
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

LEDGER_OPERATION_CONFIG: Dict[str, int] = {
    "DAILY_REWARD": 1,
    "SIGNUP_CREDIT": 3,
    "CREDIT_SPEND": -1,
    "CREDIT_ADD": 10,
}

def create_ledger_operation(name: str, extra_operations: Dict[str, str]) -> Type[Enum]:
    """Factory function to create app-specific ledger operations"""
    
    # Combine shared and app-specific operations
    operations = {
        **{op.name: op.value for op in SharedLedgerOperation},
        **extra_operations
    }
    
    return Enum(name, operations) 