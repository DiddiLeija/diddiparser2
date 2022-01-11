"""
Subprocessing: Make subprocesses as DiddiScript functions.
"""

import subprocess
import sys

from diddiparser2.messages import run_error

DIDDISCRIPT_FUNCTIONS = ("run_command", "run_python_cmd")


def build_command(*args):
    "Build and format a tuple of commands and return a string."
    final = ""
    for pos in range(len(args)):
        final += args[pos]
        final += " " if pos != len(args) - 1 else ""
    return final


def run_command(*cmd):
    "Run a command, as a subprocess"
    try:
        subprocess.run(*cmd)
    except Exception as exc:
        run_error(
            f"The subprocess '{build_command(*cmd)}' failed with error: '{str(exc)}' ({type(exc).__name__})"
        )


def run_python_cmd(*cmd):
    "Execute a Python command, as '{python executable} {arguments}'"
    try:
        subprocess.run([sys.executable] + list(*cmd))
    except Exception as exc:
        run_error(
            f"The subprocess '{build_command(*cmd)}' failed with error: '{str(exc)}' ({type(exc).__name__})"
        )
