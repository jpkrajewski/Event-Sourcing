from typing import Callable, Dict, Tuple
from menus.base_menu import Menu
from inspect import getfullargspec


class SimpleMenu(Menu):
    def __init__(self, mapped_functions: Dict[int, Tuple[Callable, str]]):
        self._mapped = mapped_functions
        self._render_menu()

    def _render_menu(self):
        string = []
        string.append("Choose one of the following options:")
        for key, value in self._mapped.items():
            string.append(f"{key}: {value[1]}")
        string.append("q: Quit")
        self._menu = "\n".join(string)

    def _create_choice_input(self, f):
        def wrapper(*args, **kwargs):
            args = getfullargspec(f).annotations  # names of arguments and their types
            for name, arg_type in args.items():
                user_input = input(f"Enter {name.replace('_', ' ')}: ")
                try:
                    argument = arg_type(user_input)
                except ValueError:
                    print(f"ERROR: {name} must be of type '{arg_type.__name__}'")
                    return
                args[name] = argument
            f(**args)

        return wrapper

    def _info_separator(self, f):
        def wrapper(*args, **kwargs):
            print("=====================================")
            print("\n\n")
            f(*args, **kwargs)
            print("\n\n")
            print("=====================================")

        return wrapper

    def _invoke_choice(self, f):
        f = self._create_choice_input(f)
        f = self._info_separator(f)
        f()

    def show(self):
        while True:
            print(self._menu)
            choice = input("Enter your choice: ")
            if choice == "q":
                break
            if choice.isdigit():
                self._invoke_choice(f=self._mapped[int(choice)][0])
            else:
                print("Wrong choice!")
