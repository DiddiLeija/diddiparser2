.. _lib-subprocessing:

``subprocessing`` -- Make subprocesses as DiddiScript functions
===============================================================

This library has functions to run processes, like if they were
called from a terminal.

Functions
---------

.. py:function:: run_command(*cmd)

   :param cmd: Each part of the command.

   Run *cmd*. It becomes a list of parts to run a command.

   .. admonition:: Example

      For example, to run ``pip --version``:

      ::

         run_command("pip", "--version");

.. py:function:: run_python_cmd(*cmd)

   :param cmd: The arguments passed to Python.

   *New since 1.1.0.*

   Run the ``python`` command with arguments *cmd*. It
   uses `sys.executable <https://docs.python.org/3/library/sys.html#sys.executable>`_
   to run things.
