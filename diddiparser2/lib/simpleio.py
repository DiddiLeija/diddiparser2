"""
SimpleIO: Common Python I/O interactions

(To file I/O, refer to FileIO)
"""

import sys
import time

from diddiparser2.diddiscript_types import Floating, Integer, Text
from diddiparser2.messages import run_error, show_warning

DIDDISCRIPT_FUNCTIONS = ("program_exit", "print_text", "print_line", "store_input", "wait")


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


def print_text(*txt):
    "Print something on the screen."
    print(*txt, end="")


def print_line(*txt):
    "Print something, plus a newline."
    print(*txt)


def store_input(msg):
    "Ask and save inputs."
    try:
        text = input(msg)
    except KeyboardInterrupt:
        run_error("Input request was interrupted by user!")
    return Text(text)


def warning(msg):
    "Show a warning."
    show_warning(str(msg))


def wait(amount):
    """
    Wait for {amount} seconds of time.
    Both floats and ints are accepted.
    """
    if not isinstance(amount, Floating) and not isinstance(amount, Integer):
        run_error(f"Expected Floating or Integer types, but got type '{type(amount).__name__}'")
    time.sleep(amount.value)
