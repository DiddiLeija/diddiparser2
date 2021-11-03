"""
SimpleIO: Common Python I/O interactions

(To file I/O, refer to FileIO)
"""

import sys

from diddiparser2.messages import run_error, show_warning

DIDDISCRIPT_FUNCTIONS = ("program_exit", "print_text", "store_input", "print_input")


class TextContainer:
    "Keep the inputs, and retrieve them."

    def __init__(self):
        self.text = None

    def store_text(self, text):
        self.text = text

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


def print_input(arg):
    "Print the stored input, if available. Also, enable the usage of indexes."
    if len(arg) >= 1:
        show_warning(f"No arguments are accepted here, but we got '{arg}'.")
    stored = INPUTS.get_text()
    if stored is None:
        run_error("There's no input stored!")
    print(stored)
