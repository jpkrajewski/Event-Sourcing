from dataclasses import dataclass
from transactions.dataclasses import Transaction


@dataclass
class Block:
    transaction: Transaction
    prev: "Block" = None
