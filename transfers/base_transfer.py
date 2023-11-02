from abc import ABC, abstractmethod
from transactions.dataclasses import Transaction
from accounts.account import Account


class Transfer(ABC):
    @staticmethod
    @abstractmethod
    def deposit(account: Account, title: str, amount: int) -> Transaction:
        ...

    @staticmethod
    @abstractmethod
    def withdraw(account: Account, title: str, amount: int) -> Transaction:
        ...

    @staticmethod
    @abstractmethod
    def transfer(
        from_account: Account, to_account: Account, title: str, amount: int
    ) -> Transaction:
        ...
