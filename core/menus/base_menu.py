from abc import ABC, abstractmethod
from typing import Dict, Tuple, Callable


class Menu(ABC):
    @abstractmethod
    def __init__(self, mapped_functions: Dict[int, Tuple[Callable, str]]) -> None:
        ...

    @abstractmethod
    def show(self):
        ...
