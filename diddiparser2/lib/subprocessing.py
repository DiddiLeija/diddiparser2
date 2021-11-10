"""
Subprocessing: Make subprocesses as DiddiScript functions.
"""

import shlex
import subprocess
import sys
import traceback

from diddiparser2.messages import run_error

DIDDISCRIPT_FUNCTIONS = ("run_command", "run_python_code")

# TODO: Find a better way to define PYTHON_GLOBALS.
# By default, the globals are the same than
# the globals(), but the locals are a bit
# different.
PYTHON_GLOBALS = globals()
PYTHON_LOCALS = {"__name__": "__console__", "__doc__": None}


def run_command(cmd):
    "Run a command, as a subprocess"
    try:
        parsed_cmd = shlex.split(cmd)
        subprocess.run(parsed_cmd, shell=True)
    except Exception as exc:
        run_error(
            f"The subprocess '{cmd}' failed with error: '{str(exc)}' ({type(exc).__name__})"
        )


def run_python_code(cmd):
    "Execute a line of Python code."
    try:
        # execute the command as-is
        exec(cmd, PYTHON_GLOBALS, PYTHON_LOCALS)
    except KeyboardInterrupt:
        run_error("Operation interrupted by user")
    except Exception:
        # Simulate an exception, but using fancy
        # DiddiParser functions.
        exc_type, value, tb = sys.exc_info()
        sys.last_type = exc_type
        sys.last_value = value
        sys.last_traceback = tb
        run_error(
            f"The Python code '{cmd}' raised this error:"
            f"\n{traceback.format_exception(exc_type, value, sys.last_traceback)}"
        )
