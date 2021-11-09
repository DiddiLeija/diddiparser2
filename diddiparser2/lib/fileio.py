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
        for line in file:
            print(file)
    except Exception as e:
        run_error(f"'{type(e).__name__}: {str(e)}'")
    del(file)


def ensurefile(path):
    "Just find a file, and print the results."
    if os.path.exists(path):
        if os.access(path):
            print(f"You can access to '{path}'")
        else:
            print(f"'{path}' exists, but it is forbidden")
    else:
        print(f"The '{path}' file does not exists")


def store_file(path):
    if not os.access(path):
        run_error("File is not accessible")
    STORED_FILE.store(io.open(path))


def print_stored(arg):
    if arg:
        show_warning("No arguments were required, but one argument was specified")
    if STORED_FILE.file is None:
        run_error("No such file stored")
    for line in STORED_FILE.file:
        print(line)
