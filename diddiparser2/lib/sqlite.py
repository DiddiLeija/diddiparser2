"""
SQLite: Interact with SQLite databases.
"""

import sqlite3
import warnings

from diddiparser2.messages import run_error, show_warning

# TODO: We have to fix the SQLite functions, return types,
#       polish some possible failures, and update the tests.
#       By now, we send a warning.
# NOTE: The warning will be only shown out of the execution,
#       because it seems like "importlib.import_module" (used
#       in the main parser) would supress the output.
warnings.warn(
  "This library ('sqlite') is in development, and its API and usage is not stable. Use it under your own risk.",
  stacklevel=2,
)

DIDDISCRIPT_FUNCTIONS = (
  "open_database",
  "close_database",
  "commit_changes",
  "execute_sql",
)


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

    def execute_command(self, cmd):
        "Execute an SQL command."
        self.cursor.execute(cmd)
        self.last_fetch = self.cursor.fetchone()[0]
        self.all_fetches = self.cursor.fetchall()


DATABASE_STORAGE = DatabaseStorage()


def open_database(path):
    "Open an SQLite database."
    DATABASE_STORAGE.connect_with_db(path)


def close_database(arg):
    "Close everything."
    if not arg:
        show_warning("No such args expected on this function")
    DATABASE_STORAGE.clear_database()


def commit_changes(arg):
    "Commit the unsaved changes."
    if not arg:
        show_warning("No such args expected on this function")
    DATABASE_STORAGE.connection.commit()


def execute_sql(cmd):
    "Execute an SQL command."
    try:
        DATABASE_STORAGE.execute_command(cmd)
    except Exception as exc:
        run_error(
          "The SQLite database connection raised the "
          f"error: {str(exc)} ({type(exc).__name__})"
        )
