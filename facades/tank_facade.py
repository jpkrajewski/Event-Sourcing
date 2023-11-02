from typing import Dict
from uuid import UUID
from accounts.account import Account

# Znaleźć zbiornik, w którym jest najwięcej wody
# Znaleźć zbiornik, który jest najbardziej zapełniony
# Znaleźć wszystkie puste zbiorniki


class TankFacade:
    required_attributes = ("_accounts",)

    def get_tank_with_most_water(self):
        """(Tank) - Get tank with most water and print its name and amount of water."""
        tank = max(self._accounts.values(), key=lambda x: x.amount)
        print(f"Tank name: {tank.get_name()} - Amount: {tank.get_amount()}")

    def get_tank_with_most_percent_full(self):
        """(Tank) - Get tank with most percent full and print its name, amount of water and percent full."""
        tank = max(self._accounts.values(), key=lambda x: x.amount / x.max_volume)
        print(
            f"Tank name: {tank.get_name()} - Amount: {tank.get_amount()}, Percent full: {tank.amount / tank.max_volume * 100}%"
        )

    def get_empty_tanks(self):
        """(Tank) - Get all empty tanks."""
        tanks = [tank for tank in self._accounts.values() if tank.amount == 0]
        print("Empty tanks:")
        for tank in tanks:
            print(f"Tank name: {tank.get_name()} - Amount: {tank.get_amount()}")
