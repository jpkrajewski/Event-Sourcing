from enum import Enum


class OperationType(Enum):
    DEPOSIT: str = "deposit"
    WITHDRAW: str = "withdraw"
    TRANSFER: str = "transfer"
