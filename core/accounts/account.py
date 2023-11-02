from uuid import UUID
import zope.interface


class IAccount(zope.interface.Interface):
    def get_uuid() -> UUID:
        ...

    def get_name() -> str:
        ...

    def get_amount() -> int:
        ...

    def transfer(account: "IAccount", amount: int):
        ...

    def withdraw(amount: int):
        ...

    def deposit(amount: int):
        ...
