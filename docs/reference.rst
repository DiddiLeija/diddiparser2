.. _api-reference:

API reference of DiddiParser 2
==============================

This document explains the internal API of DiddiParser 2

.. py:module:: diddiparser2.parser

.. py:class:: DiddiParser

   This class is the main DiddiScript parser.

   .. py:method:: __init__(self, file)
                  __init__(self, file, ignore_suffix=False)

      :param str file: The DiddiScript file to be parsed.
      :param bool ignore_suffix: If ``True``, tells DiddiParser to ignore the suffix mismatch.
   
      The constructor method. It reads the selected filename, and gets the commands via
      :py:meth:`diddiparser2.parser.DiddiParser.get_commands`.
   
   .. py:method:: get_commands(self)
   
      :return: A list of prepared commands.
      :rtype: list
      :raises diddiparser2.messages.error: When a syntax error is found.
      
      This function returns a list of DiddiScript commands, without comments. It can raise
      a compile error if there are missing semicolons (;).
   
   .. py:method:: executeline(self, line)
   
      :param str line: A line of DiddiScript code.
      :raises diddiparser2.messages.error: If the execution fails.
      
      Run a single line of code.
      
   .. py:method:: runfile(self)
      
      Runs :py:meth:`diddiparser2.parser.DiddiParser.executeline` for each line, and
      then prints a success message.

.. py:data:: TOOL_FUNCTIONS
   
   :type: tuple
   :value: ("load_module", "load_extension")
   
   A tuple of special DiddiScript functions.

.. py:data:: MODULE_FUNCTIONS

   :type: dict
   :value: {}
   
   A ``name: callable`` dictionary.
