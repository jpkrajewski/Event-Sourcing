from typing import Dict, Tuple, Callable
import zope.interface


class IMenu(zope.interface.Interface):
    def __init__(mapped_functions: Dict[int, Tuple[Callable, str]]) -> None:
        ...

    def show():
        ...
