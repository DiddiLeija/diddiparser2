"""
SQLite: Interact with SQLite databases.
"""

import sqlite3

from diddiparser2.diddiscript_types import Boolean, Floating, Integer, Null, Text
from diddiparser2.messages import run_error, show_warning

DIDDISCRIPT_FUNCTIONS = (
  "open_database",
  "close_database",
  "commit_changes",
  "execute_sql",
)


def _convert_py_to_diddi(data):
    "Convert the DiddiScript value 'data' into a Python standardized value."
    if isinstance(data, Null):
        return None
    elif isinstance(data, Text):
        return str(data)
    elif isinstance(data, Integer):
        return int(data)
    elif isinstance(data, Floating):
        return float(data)
    elif isinstance(data, Boolean):
        return bool(data)
    else:
        run_error(f"Unrecognized type to convert: {type(data).__name__}")


class DatabaseStorage:
    "Store the database contents."
    connection = None
    cursor = None
    all_fetches = None
    last_fetch = None

    def clear_database(self):
        "Clear everything: database connection, cursor and memories"
        if self.connection.in_transaction:
            # some changes will be lost, warn about it
            show_warning(
              "You tried to close a database with uncommited changes. "
              "The changes will be lost."
            )
        self.cursor.close()
        self.connection.close()
        self.last_fetch = None
        self.all_fetches = None

    def connect_with_db(self, path):
        "Connect with a SQLite database"
        if self.connection is not None:
            # something's living there, so let's
            # close everything
            self.clear_database()
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def execute_command(self, *cmd_and_args):
        "Execute an SQL command."
        # First of all, break the args
        # into cmd + optional args.
        # Currently, args are only supported
        # in qmark style, no named style yet.
        args = []
        for arg in cmd_and_args:
            args.append(_convert_py_to_diddi(arg))
        args = tuple(args)
        cmd = args[0]
        if len(args) > 1:
            # there are args over there
            args = args[1:]
        else:
            # no args, so there's no need to
            # work on this.
            args = tuple()
        self.cursor.execute(cmd, args)
        self.last_fetch = self.cursor.fetchone()[0]
        self.all_fetches = self.cursor.fetchall()


DATABASE_STORAGE = DatabaseStorage()


def open_database(path):
    "Open an SQLite database."
    if not isinstance(path, Text):
        run_error(f"Expected a Text object as 'path', but got type '{type(path).__name__}'.")
    DATABASE_STORAGE.connect_with_db(str(path))
    return Null()


def close_database(arg):
    "Close everything."
    if not arg:
        show_warning("No such args expected on this function")
    DATABASE_STORAGE.clear_database()
    return Null()


def commit_changes(arg):
    "Commit the unsaved changes."
    if not arg:
        show_warning("No such args expected on this function")
    DATABASE_STORAGE.connection.commit()
    return Null()


def execute_sql(*args):
    "Execute an SQL command."
    try:
        DATABASE_STORAGE.execute_command(*args)
    except Exception as exc:
        run_error(
          "The SQLite database connection raised the "
          f"following error: {str(exc)} ({type(exc).__name__})"
        )
