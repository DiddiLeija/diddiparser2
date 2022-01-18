"""
A builtin DiddiScript module, to provide libraries by default.
"""

import os

from diddiparser2.lib import simpleio

DIDDISCRIPT_FUNCTIONS = ["chdir", "cd", "print_text", "print_line", "store_input"]


def cd(arg):
    os.chdir(str(arg))


# The "cd / chdir", which replaces the standard
chdir = cd
# Stuff imported from simpleio
print_text = simpleio.print_text
print_line = simpleio.print_line
store_input = simpleio.store_input
