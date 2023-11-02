from uuid import UUID


class AccountFacade:
    required_attributes = ("_accounts",)

    def list_accounts(self):
        """(Account) - List all accounts."""
        for uuid, account in self._accounts.items():
            print(f"{uuid}: {account.get_name()}")

    def get_account_details(self, uuid: UUID):
        """(Account) - Get account details."""
        account = self._accounts[uuid]
        print(f"{account.get_name()} - Amount: {account.get_amount()}")
