"""
FileIO: DiddiScript library for handling files.
"""

import io
import os

from diddiparser2.messages import run_error, show_warning

DIDDISCRIPT_FUNCTIONS = (
    "printfile",
    "ensurefile",
    "store_file",
    "print_stored",
)


class StoredFile:
    "A space to store files."
    file = None

    def store(self, stream):
        self.file = stream


STORED_FILE = StoredFile()


def printfile(path):
    "Find and print a file."
    if not os.path.exists(path):
        run_error(f"File '{path}' does not exists")
    try:
        file = io.open(path)
        for line in file.readlines():
            print(file)
    except Exception as e:
        run_error(f"'{type(e).__name__}: {str(e)}'")
    del(file)


def ensurefile(path):
    "Just find a file, and print the results."
    if os.path.exists(path):
        # The use of os.access is harmless here, because
        # we don't want to use the file by ourselves.
        # However, a user can get confused when
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
        STORED_FILE.store(io.open(path).readlines())
    except PermissionError:
        run_error(f"File '{path}' is restricted")


def print_stored(arg):
    if arg:
        show_warning("No arguments were required, but one argument was specified")
    if not STORED_FILE.file:
        run_error("No such file stored")
    for line in STORED_FILE.file:
        print(line)
