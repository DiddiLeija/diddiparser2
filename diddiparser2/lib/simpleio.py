"""
SimpleIO: Common Python I/O interactions

(To file I/O, refer to FileIO)
"""

import sys

from diddiparser2.diddiscript_types import Floating, Integer, Text
from diddiparser2.messages import run_error

DIDDISCRIPT_FUNCTIONS = ("program_exit", "print_text", "print_line", "store_input")


def program_exit(msg):
    "Exit (via sys.exit) with a message or an exit code."
    try:
        if isinstance(msg, Floating) or isinstance(msg, Integer):
            msg = int(msg)
        else:
            msg = str(msg)
    except Exception:
        pass
    sys.exit(msg)


def print_text(txt):
    "Print something on the screen."
    print(txt, end="")


def print_line(txt):
    "Print something, plus a newline."
    print(txt)


def store_input(msg):
    "Ask and save inputs."
    try:
        text = input(msg)
    except KeyboardInterrupt:
        run_error("Input request was interrupted by user!")
    return Text(text)
