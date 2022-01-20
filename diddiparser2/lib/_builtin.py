"""
A builtin DiddiScript module, to provide libraries by default.
"""

import importlib
import os

from diddiparser2.diddiscript_types import Text
from diddiparser2.lib import simpleio
from diddiparser2.messages import run_error, show_warning

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
FUNCTIONS_ORIGINS = dict()


# A "cd" function
def cd(arg=None):
    if isinstance(arg, Text):
        os.chdir(str(arg))
    elif arg is not None:
        run_error(f"Unexpected parameter to change cwd: {arg}")
    return Text(os.getcwd())


# The "chdir" alias
chdir = cd
# Stuff imported from simpleio
print_text = simpleio.print_text
print_line = simpleio.print_line
store_input = simpleio.store_input


# "load_module"
def load_module(*args):
    for arg in args:
        arg = str(arg)
        mod = importlib.import_module(f"diddiparser2.lib.{arg}")
        mod_list = mod.DIDDISCRIPT_FUNCTIONS
        for item in mod_list:
            exec(
                f"from diddiparser2.lib.{arg} import {item} as element; MODULE_FUNCTIONS['{item}'] = element",
                locals(),
                globals(),
            )
            FUNCTIONS_ORIGINS[item] = ("module", arg)


# "load_extension"
def load_extension(*args):
    for arg in args:
        # A Python-like import is expected. For
        # example: "module", "pkg.module"
        arg = str(arg)
        ext = importlib.import_module(f"{arg}")
        ext_list = ext.DIDDISCRIPT_FUNCTIONS
        for item in ext_list:
            exec(
                f"from {arg} import {item} as element; MODULE_FUNCTIONS['{item}'] = element",
                locals(),
                globals(),
            )
            FUNCTIONS_ORIGINS[item] = ("extension", arg)


# "print_available_functions"
def print_available_functions(arg=None):
    if arg:
        show_warning("This function is not currently accepting arguments.")
    print_line("---- Loaded functions ----")
    for item in MODULE_FUNCTIONS:
        kind, name = FUNCTIONS_ORIGINS[item]
        print_line(f"  {item} (loaded from {kind} '{name}')")
