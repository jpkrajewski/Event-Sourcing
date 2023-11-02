import unittest

from main import BlockChain, Block, Tank, Transaction, Account


class TestBlockChain(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account(
            tanks=[
                Tank("tank1", 100),
                Tank("tank2", 300),
            ]
        )
        super().setUp()

    def test_get_failed_transaction_uuid(self):
        tank = self.account.get_tank_by_name("tank2")
        for n in range(6):
            title = f"Failed pour number: {n+1}"
            self.account.pour_water(tank, title, 500)

        tank = self.account.get_tank_by_name("tank1")
        for n in range(10):
            title = f"Failed pour number: {n+1}"
            self.account.pour_water(tank, title, 300)
        failed_uuid = self.account.get_most_failed_transactions_uuid()
        self.assertEqual(tank.uuid, failed_uuid["uuid"])
        self.assertEqual(10, failed_uuid["count"])


if __name__ == "__main__":
    unittest.main()
