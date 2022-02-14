.. _lib-sqlite:

``sqlite`` -- Interact with SQLite databases
============================================

This library provides an interface to the
`sqlite3 Python module <https://docs.python.org/3/library/sqlite3.html>`_.
With this, you can open databases, and execute SQL commands on it.

.. warning::

   This library is in development, and its API and usage is not stable.
   Use it under your own risk. Proofs of this are:

   * A ``warnings.warn`` at the beginning of the Python module
     (unfortunately, the warning is suppressed by ``importlib``
     while loading the module)

   * A warning in the development tests

Functions
---------

.. py:function:: open_database(path)

   :param path: The database file name.

   This function generates a connection with the database
   *path*. It also creates a cursor to execute the SQL
   commands.

   .. note::

      The keyword ``:memory:`` can be used as *path* to open
      a database in the memory.

   .. warning::

      If you open a database, while you have another connection
      with unsaved changes, the changes will be lost, and the previous
      database will be closed.

.. py:function:: close_database()

   This closes everything on the database (connection, cursor
   and memory data).

   .. warning::

      If you have unsaved changes on the database, this function
      will delete them. They won't be saved.

      Before closing a database, get sure to run the ``commit_changes``
      function (see below).

.. py:function:: commit_changes()

   This function saves every unsaved change to the database. Get sure
   to run this before closing the file or exiting from the program!

.. py:function:: execute_sql(cmd)

   :param cmd: The SQL command.

   Run a single line of SQL commands, that are passed to the cursor. The
   changes will wait for a ``commit_changes()`` call to save the changes
   caused by the command.
