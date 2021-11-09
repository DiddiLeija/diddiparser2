.. _lib-subprocessing:

``subprocessing`` -- Make subprocesses as DiddiScript functions
===============================================================

This library has functions to run processes, like if they were
called from a terminal.

Functions
---------

.. py:function:: run_command(cmd)

   :param cmd: The whole command.

   Run a command *cmd*. It is parsed to get a list of
   commands and arguments. If something (while parsing or running),
   a run error will be shown.

.. py:function:: run_python_code(cmd)

   :param cmd: A line of valid Python code.

   Execute a single line of code using the standard
   `exec() function <https://docs.python.org/3/library/functions.html#exec>`_.
   It uses customized globals and locals, that are shared between each
   ``run_python_code`` call.

   .. note::

      The Python code passed to this function will be interpreted with
      the same Python interpreter than the one that executed the parser.

      Let's imagine that you are running DiddiParser with a Python
      3.8 interpreter. However, on your DiddiScript code, you called
      a ``run_python_code`` function that uses Python 3.10 syntax:

      ::

          load_module("subprocessing");

          run_python_code("import sys");
          run_python_code("match sys.platform:");  !# Python 3.10 syntax

      This example will crash, because Python 3.6 doesn't support ``match/case``
      blocks.
