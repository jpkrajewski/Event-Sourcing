import pytest

from core.facades.tank_facade import TankFacade
from core.tanks.tank import Tank


@pytest.fixture
def tanks():
    tanks = {}
    for n in range(10):
        tank = Tank(f"Tank {n+1}", 100)
        tank.amount = (n + 1) * 10
        tanks[tank.get_uuid()] = tank
    return tanks


@pytest.fixture
def facade(tanks):
    facade = TankFacade()
    facade._accounts = tanks
    return facade


def test_get_tank_with_most_water(facade, capsys):
    facade.get_tank_with_most_water()
    captured = capsys.readouterr()
    assert captured.out == "Tank name: Tank 10 - Amount: 100\n"


def test_get_tank_with_most_percent_full(facade, capsys):
    facade.get_tank_with_most_percent_full()
    captured = capsys.readouterr()
    assert captured.out == "Tank name: Tank 10 - Amount: 100, Percent full: 100.0%\n"


def test_get_empty_tanks(facade, capsys):
    facade.get_empty_tanks()
    captured = capsys.readouterr()
    assert captured.out == "Empty tanks:\n"
