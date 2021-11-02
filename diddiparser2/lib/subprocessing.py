"""
Subprocessing: Make subprocesses as DiddiScript functions.
"""

import shlex
import subprocess

from diddiparser2.exceptions import run_error

DIDDISCRIPT_FUNCTIONS = "run_command"


def run_command(cmd):
    "Run a command, as a subprocess"
    try:
        parsed_cmd = shlex.split(cmd)
        subprocess.run(parsed_cmd, shell=True)
    except Exception as exc:
        run_error(
            f"The subprocess '{cmd}' failed with error: '{str(exc)}' ({type(exc).__name__})"
        )
