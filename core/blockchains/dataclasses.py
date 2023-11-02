from dataclasses import dataclass
from core.transactions.dataclasses import Transaction


@dataclass
class Block:
    transaction: Transaction
    prev: "Block" = None
