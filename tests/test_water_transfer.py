import pytest

from core.tanks.tank import Tank
from core.transfers.water_transfer import WaterTransfer


@pytest.fixture
def tank():
    tank = Tank("Tank 1", 100)
    tank.amount = 50
    return tank


@pytest.fixture
def tank_helper():
    tank = Tank("Tank 1", 100)
    tank.amount = 50
    return tank


@pytest.mark.parametrize(
    "volume, expected",
    [
        (50, True),
        (100, False),
    ],
)
def test_deposit(tank, volume, expected):
    transaction = WaterTransfer.deposit(tank, f"Deposit {volume}", volume)
    assert transaction.status == expected


@pytest.mark.parametrize(
    "volume, expected",
    [
        (50, True),
        (100, False),
    ],
)
def test_successfull_withdraw(tank, volume, expected):
    transaction = WaterTransfer.withdraw(tank, f"Withdraw {volume}", volume)
    assert transaction.status == expected


@pytest.mark.parametrize(
    "volume, expected",
    [
        (50, True),
        (100, False),
    ],
)
def test_failed_withdraw(tank, tank_helper, volume, expected):
    transaction = WaterTransfer.transfer(tank, tank_helper, f"Transfer {volume}", volume)
    assert transaction.status == expected
