from core.tanks.tank import Tank
from core.blockchains.blockchain import BlockChain
from core.transfers.water_transfer import WaterTransfer
from core.facades.facade import Facade
from core.menus.simple_menu import SimpleMenu

if __name__ == "__main__":
    # Instantiate the dependencies
    blockchain = BlockChain()
    transfer = WaterTransfer()
    accounts = {}
    for n in range(10):
        account = Tank(f"Tank {n+1}", ((n + 1) * 100))
        accounts[account.get_uuid()] = account

    # Instantiate the facade
    facade = Facade(
        blockchain=blockchain, accounts=accounts, transfer=transfer, menu=SimpleMenu
    )
    facade.run()
