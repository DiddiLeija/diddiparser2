"""
SimpleIO: Common Python I/O interactions

(To file I/O, refer to FileIO)
"""

import sys

from diddiparser2.diddiscript_types import Null, Text
from diddiparser2.messages import run_error

DIDDISCRIPT_FUNCTIONS = ("program_exit", "print_text", "store_input")


class TextContainer:
    "Keep the inputs, and retrieve them."

    def __init__(self):
        self.text = Null()

    def store_text(self, text):
        self.text = Text(text)

    def get_text(self):
        return self.text


INPUTS = TextContainer()


def program_exit(msg):
    "Exit (via sys.exit) with a message or an exit code."
    try:
        msg = int(msg)
    except Exception:
        pass
    sys.exit(msg)


def print_text(txt):
    "Print something on the screen, with no color."
    print(txt)


def store_input(msg):
    "Ask and save inputs."
    try:
        text = input(msg)
    except KeyboardInterrupt:
        run_error("Input request was interrupted by user!")
    INPUTS.store_text(text)
    return INPUTS.get_text()
