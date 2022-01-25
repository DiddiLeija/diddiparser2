"""
This is a copy of the extension example found at
DSGP 3. Whenever the original example is modified,
this file should be updated too.
"""

from diddiparser2.diddiscript_types import Null
from diddiparser2.lib.simpleio import print_line
from diddiparser2.messages import show_warning

DIDDISCRIPT_FUNCTIONS = ("my_func", "my_func2")


def my_func(some_arg):
    print_line(f"Hello! I received a {some_arg}")


def my_func2(*args):
    for arg in args:
        if isinstance(arg, Null):
            show_warning("Found a Null!")
        else:
            print_line(f"Found a {arg}!")


def my_func3():
    # This function won't be accesible for DiddiScript, though
    # it can be easily used by Python. This is because "my_func3"
    # is not in DIDDISCRIPT_FUNCTIONS.
    pass
