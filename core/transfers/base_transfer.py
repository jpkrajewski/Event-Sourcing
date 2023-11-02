from core.transactions.dataclasses import Transaction
from core.accounts.account import IAccount
import zope.interface


class ITransfer(zope.interface.Interface):
    def deposit(account: IAccount, title: str, amount: int) -> Transaction:
        ...

    def withdraw(account: IAccount, title: str, amount: int) -> Transaction:
        ...

    def transfer(from_account: IAccount, to_account: IAccount, title: str, amount: int) -> Transaction:
        ...
