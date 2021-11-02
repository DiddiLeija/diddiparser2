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
