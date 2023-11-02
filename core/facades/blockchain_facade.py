from core.blockchains.blockchain import BlockChain
from core.accounts.account import IAccount
from core.transactions.enums import OperationType
from uuid import UUID


class BlockChainFacade:
    required_attributes = ("_accounts", "_blockchain")

    def get_most_failed_transactions_uuid(self):
        """(Blockchain) - Get the UUID of the account with the most failed transactions."""
        counter = {k: 0 for k in self._blockchain.blocks.keys()}
        for key, block in self._blockchain.blocks.items():
            while block is not None:
                if block.transaction.status is False:
                    counter[key] += 1
                block = block.prev
        uuid = max(counter, key=counter.get)
        print(f"UUID: {uuid} - Count: {counter[uuid]}")

    def get_most_operations_transactions_uuid(self, operation: OperationType):
        """(Blockchain) - Get the UUID of the account with the most operations of a given type."""
        counter = {k: 0 for k in self._blockchain.blocks.keys()}
        for key, block in self._blockchain.blocks.items():
            while block is not None:
                if block.transaction.operation == operation:
                    counter[key] += 1
                block = block.prev
        uuid = max(counter, key=counter.get)
        print(f"UUID: {uuid} - Count: {counter[uuid]}")

    def get_history(self, uuid: UUID):
        """(Blockchain) - Get the history of transactions for a given account."""
        block: BlockChain = self._blockchain.blocks[uuid]
        if not block:
            return
        while block is not None:
            print(
                f"TIMESTAMP: {block.transaction.timestamp}"
                f" - TITLE: {block.transaction.title} | "
                f"AMOUNT: {block.transaction.amount} | "
                f"OPERATION: {block.transaction.operation}"
            )
            block = block.prev

    def check_state(self, uuid: UUID):
        """(Blockchain) - Check if the state of a given account is correct."""
        account: IAccount = self._accounts[uuid]
        block: BlockChain = self._blockchain.blocks[uuid]
        amount = 0
        if not block:
            return amount
        while block is not None:
            if block.transaction.operation == OperationType.DEPOSIT:
                amount += block.transaction.amount
            elif block.transaction.operation == OperationType.WITHDRAW:
                amount -= block.transaction.amount
            elif block.transaction.operation == OperationType.TRANSFER:
                amount -= block.transaction.amount
            block = block.prev
        if amount == account.amount:
            print(f"State is correct: Account amount: {account.amount} | BlockChain amount: {amount}")
        else:
            print(f"State is incorrect: Account amount: {account.amount} | BlockChain amount: {amount}")
