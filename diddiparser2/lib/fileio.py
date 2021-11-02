"""
FileIO: DiddiScript library for handling files.
"""

import io
import os

from colorama import Fore

from diddiparser2.messages import run_error

DIDDISCRIPT_FUNCTIONS = ("printfile", "ensurefile")


def printfile(path):
    "Find and print a file."
    if not os.path.exists(path):
        run_error(f"File '{path}' does not exists")
    try:
        file = io.open(path)
        for line in file:
            print(file)
    except Exception as e:
        run_error(f"'{type(e).__name__}: {str(e)}'")


def ensurefile(path):
    "Just find a file, and print the results."
    if os.path.exists(path):
        if os.access(path):
            print(f"You can access to '{path}'")
        else:
            print(f"'{path}' exists, but it is forbidden")
    else:
        print(f"The '{path}' file does not exists")
