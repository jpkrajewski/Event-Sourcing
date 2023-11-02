from abc import ABC, abstractmethod
from uuid import UUID


class Account(ABC):
    @abstractmethod
    def get_uuid(self) -> UUID:
        ...

    @abstractmethod
    def get_name(self) -> str:
        ...

    @abstractmethod
    def get_amount(self) -> int:
        ...

    @abstractmethod
    def transfer(self, account: "Account", amount: int):
        ...

    @abstractmethod
    def withdraw(self, amount: int):
        ...

    @abstractmethod
    def deposit(self, amount: int):
        ...
