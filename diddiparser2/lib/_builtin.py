"""
A builtin DiddiScript module, to provide libraries by default.
"""

import importlib
import os

from diddiparser2.lib import simpleio
from diddiparser2.messages import show_warning

DIDDISCRIPT_FUNCTIONS = (
    "chdir",
    "cd",
    "print_text",
    "print_line",
    "store_input",
    "load_module",
    "load_extension",
    "print_available_functions",
)
MODULE_FUNCTIONS = dict()


# A "cd" function
def cd(arg):
    os.chdir(str(arg))
    return arg


# "load_module"
def load_module(*args):
    for arg in args:
        mod = importlib.import_module(f"diddiparser2.lib.{arg}")
        mod_list = mod.DIDDISCRIPT_FUNCTIONS
        for item in mod_list:
            exec(
                f"from diddiparser2.lib.{arg} import {item} as element; MODULE_FUNCTIONS['{item}'] = element",
                locals(),
                globals(),
            )


# "load_extension"
def load_extension(*args):
    for arg in args:
        # A Python-like import is expected. For
        # example: "module", "pkg.module"
        ext = importlib.import_module(f"{arg}")
        ext_list = ext.DIDDISCRIPT_FUNCTIONS
        for item in ext_list:
            exec(
                f"from {arg} import {item} as element; MODULE_FUNCTIONS['{item}'] = element",
                locals(),
                globals(),
            )


# "print_available_functions"
def print_available_functions(arg):
    if arg:
        show_warning("This function is not currently accepting arguments.")
    print("---- Loaded functions ----")
    for item in MODULE_FUNCTIONS:
        print(f"  {item}")


# The "chdir" alias
chdir = cd
# Stuff imported from simpleio
print_text = simpleio.print_text
print_line = simpleio.print_line
store_input = simpleio.store_input
