from dataclasses import dataclass, field
from core.transactions.enums import OperationType
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class Transaction:
    status: bool
    title: str
    operation: OperationType
    system_message: str
    from_uuid: UUID
    to_uuid: UUID
    amount: int
    timestamp: datetime = field(default_factory=datetime.now)
