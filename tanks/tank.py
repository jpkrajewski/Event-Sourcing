from accounts.account import Account
from uuid import UUID, uuid5


class Tank(Account):
    def __init__(self, name: str, max_volume: int):
        self._uuid = uuid5(namespace=UUID(int=0), name=name)
        self._name = name
        self.amount = 0
        self.max_volume = max_volume

    def get_uuid(self) -> UUID:
        return self._uuid

    def get_name(self) -> str:
        return self._name

    def get_amount(self) -> int:
        return self.amount

    def deposit(self, volume: int):
        self.amount += volume

    def withdraw(self, volume: int):
        self.amount -= volume

    def transfer(self, tank, volume: int):
        self.withdraw(volume)
        tank.deposit(volume)

    def can_pour_in(self, volume: int) -> bool:
        return self.max_volume >= self.amount + volume

    def can_pour_out(self, volume: int) -> bool:
        return 0 <= self.amount - volume
