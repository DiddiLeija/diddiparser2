"""
FileIO: DiddiScript library for handling files.
"""

import io
import os

from diddiparser2.diddiscript_types import Null, Text
from diddiparser2.messages import run_error, show_warning

DIDDISCRIPT_FUNCTIONS = (
    "printfile",
    "ensurefile",
    "store_file",
    "print_stored",
)


class StoredFile:
    "A space to store files."
    file = Null()

    def store(self, stream):
        self.file = Text(stream.read())


STORED_FILE = StoredFile()


def printfile(path):
    "Find and print a file."
    if not os.path.exists(path):
        run_error(f"File '{path}' does not exists")
    try:
        with io.open(path) as f:
            print(f.read())
    except Exception as e:
        run_error(f"'{type(e).__name__}: {str(e)}'")


def ensurefile(path):
    "Just find a file, and print the results."
    if os.path.exists(path):
        # The use of os.access is harmless here, because
        # we don't want to use the file by ourselves.
        if os.access(path, os.X_OK):
            # We can read, write and modify the path.
            print(f"You can access to '{path}'")
        else:
            # Some restrictions apply for the path
            print(f"'{path}' exists, but it has modification restrictions")
    else:
        print(f"The '{path}' file does not exists")


def store_file(path):
    try:
        STORED_FILE.store(io.open(path))
    except PermissionError:
        run_error(f"File '{path}' is restricted")
    return STORED_FILE.file


def print_stored(arg):
    if arg:
        show_warning("No arguments were required, but one argument was specified")
    if not STORED_FILE.file.value:
        run_error("No such file stored")
    for line in str(STORED_FILE.file).splitlines():
        print(line)
