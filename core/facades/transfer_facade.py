from uuid import UUID
from core.blockchains.dataclasses import Block
from core.transactions.dataclasses import Transaction


class TransferFacade:
    required_attributes = ("_transfer", "_accounts", "_blockchain")

    def deposit(self, uuid: UUID, title: str, amount: int):
        """(Transfer) - Deposit money to an account."""
        transaction = self._transfer.deposit(self._accounts[uuid], title, amount)
        self._blockchain.add_block(Block(transaction))
        self._print_transaction(transaction)

    def withdraw(self, uuid: UUID, title: str, amount: int):
        """(Transfer) - Withdraw money from an account."""
        transaction = self._transfer.withdraw(self._accounts[uuid], title, amount)
        self._blockchain.add_block(Block(transaction))
        self._print_transaction(transaction)

    def transfer(self, from_uuid: UUID, to_uuid: UUID, title: str, amount: int):
        """(Transfer) - Transfer money between accounts."""
        amount = int(input("Enter the amount of the transaction: "))
        transaction = self._transfer.transfer(
            self._accounts[from_uuid], self._accounts[to_uuid], title, amount
        )
        self._blockchain.add_block(Block(transaction))
        self._print_transaction(transaction)

    def _print_transaction(self, transaction: Transaction):
        print("=====================================")
        print("Transaction details:")
        print(f"Transaction status: {transaction.status}")
        print(f"Transaction message: {transaction.system_message}")
        print(f"Transaction title: {transaction.title}")
        print(f"Transaction amount: {transaction.amount}")
        print(f"Transaction type: {transaction.operation.value}")
        print("=====================================")
