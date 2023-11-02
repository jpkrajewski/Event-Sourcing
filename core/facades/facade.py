from core.facades.account_facade import AccountFacade
from core.facades.blockchain_facade import BlockChainFacade
from core.facades.transfer_facade import TransferFacade
from core.facades.tank_facade import TankFacade
from core.accounts.account import IAccount
from core.blockchains.blockchain import BlockChain
from core.transfers.base_transfer import ITransfer
from core.menus.base_menu import IMenu
from uuid import UUID
from typing import Dict
import inspect


class Facade(AccountFacade, BlockChainFacade, TransferFacade, TankFacade):
    facades = (AccountFacade, BlockChainFacade, TransferFacade, TankFacade)

    def __init__(
        self,
        accounts: Dict[UUID, IAccount],
        blockchain: BlockChain,
        transfer: ITransfer,
        menu: IMenu,
    ):
        self._accounts = accounts
        self._blockchain = blockchain
        self._transfer = transfer
        self._check_required_attributes()
        self._map_functions_to_numbers()
        self._menu = menu(self.mapped)

    def _check_required_attributes(self):
        for facade in inspect.getmro(self.__class__):
            if isinstance(facade, object):  # MRO returns object as last class, we don't need it
                break
            for required in facade.required_attributes:
                if not hasattr(self, required):
                    raise AttributeError(f"Facade has no attribute self.{required} required by {facade.__name__}.")

    def _map_functions_to_numbers(self):
        self.mapped = {}
        facades_functions = [name for name in dir(self) if self._is_function_from_facade(name)]
        sorted_facades_functions = sorted(facades_functions, key=lambda x: getattr(self, x).__doc__)
        for i, name in enumerate(sorted_facades_functions):
            obj = getattr(self, name)
            self.mapped[i] = (obj, obj.__doc__)

    def _is_function_from_facade(self, name):
        obj = getattr(self, name)
        return not name.startswith("_") and obj.__doc__ is not None and callable(obj)

    def run(self):
        self._menu.show()
