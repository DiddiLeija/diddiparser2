.. _api-reference:

API reference of DiddiParser 2
==============================

This document explains the internal API of DiddiParser 2

.. py:module:: diddiparser2.diddiscript_types

``diddiparser2.diddiscript_types`` -- DiddiScript standard types
---------------------------------------------------------------

This Python module stores all the DiddiScript types (written in
Python) defined by `DSGP 1 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-001.md>`_.
You can return these types in your extensions.

.. py:class:: DiddiScriptType

   The template type for all the DiddiScript types. Please don't use this type.

   .. py:attribute:: value

      The Python value that is represented by the DiddiScript type. On this template type,
      is is an empty ``object``.

   .. py:method:: __str__(self)

      Returns the value, as a string. In most of the cases,
      this method is respected by all the subclasses.

   .. py:method:: __int__(self)

      Returns the value as a Python integer. If a ``ValueError``
      is raised, we raise our own exception.

    .. py:method:: __float__(self)

       Returns the value as a Python float. If a ``ValueError``
       is raised, we raise our own exception.

    .. py:method:: __bool__(self)

       Returns the value as a Python bool.

.. py:class:: Integer(DiddiScriptType)

   The type that represents integer numbers.

   .. py:method:: __init__(self, value_text)

      :param value_text: The value to be stored. This becomes :py:attr:`diddiparser2.diddiscript_types.DiddiScriptType.value`.

      Constructor method. The value is converted to ``int``.

   .. py:method:: __int__(self)

      Instead of trying to convert to ``int``, we just return the value.

.. py:class:: Floating(DiddiScriptType)

   The type that represents floating numbers.

   .. py:method:: __init__(self, value_text)

      :param value_text: The value to be stored. This becomes :py:attr:`diddiparser2.diddiscript_types.DiddiScriptType.value`.

      Constructor method. The value is converted to ``float``.

   .. py:method:: __float__(self)

      Instead of trying to convert to ``float``, we just return the value.

.. py:class:: Text(DiddiScriptType)

   The type that represents text.

   .. py:method:: __init__(self, value_text)

      :param value_text: The value to be stored. This becomes :py:attr:`diddiparser2.diddiscript_types.DiddiScriptType.value`.

      Constructor method. The value is not converted, since we *always* expect ``value`` to be a string.

.. py:class:: Boolean(DiddiScriptType)

   The type that represents booleans.

   .. py:method:: __init__(self, value_text)

      :param value_text: The value to be stored. This becomes :py:attr:`diddiparser2.diddiscript_types.DiddiScriptType.value`.

      Constructor method. It tries to convert the value to ``bool``. If that doesn't work, we convert value to the bool
      resulting from a truthy-falsy comparation (however, this is not needed at all).

    .. py:method:: __bool__(self)

       Instead of trying to convert to ``bool``, we just return the value.

.. py:class:: Null(DiddiScriptType)

   The type that represents a null value.

   .. py:method:: __init__(self, value_text=None)

      :param value_text: We only have this to avoid argument issues, but it is ignored.

      Constructor method. Actually, ``value_text`` is ignored here, we store ``None`` instead.

   .. py:method:: __str__(self)

      This method is overriden to return a ``"Null"`` text.

.. py:module:: diddiparser2.parser

``diddiparser2.parser`` -- main parser configurations
-----------------------------------------------------

This module configures the main DiddiScript parser, and
some useful variables.

.. py:data:: __version__

   :type: str

   A string that represents the parser's version.

.. py:data:: EXECUTION_VARIABLES

   :type: dict
   :value: {}

   A ``name: value`` dictionary of defined variables.

.. py:class:: DiddiParser

   This class is the main DiddiScript parser.

   .. py:method:: __init__(self, file, ignore_suffix=False, verbose=False, compile_only=False, notify_success=True)

      :param str file: The DiddiScript file to be parsed.
      :param bool ignore_suffix: If True, tells DiddiParser to ignore the suffix mismatch.
      :param bool verbose: If True, the parser will echo all the commands
                           executed by :py:meth:`diddiparser2.parser.DiddiParser.runfile`.
      :param bool compile_only: If True, the parser will just run what is necessary for
                                compiling (like library loaders and variable definitions),
                                and will try to find potential errors (unresolved references,
                                invalid code, etc.).
      :param bool notify_success: Mostly an internally-used option, to avoid notifying when an
                                  execution finishes without issues.

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

      Run a single line of code. It runs :py:meth:`diddiparser2.parser.DiddiParser.execute_def`
      and :py:meth:`diddiparser2.parser.DiddiParser.execute_func` when necessary.

   .. py:method:: execute_def(self, line)

      :param str line: A line of DiddiScript code.
      :raises diddiparser2.messages.error: If the execution fails.

      Execute a line with a variable definition, according to DSGP 1.

      .. seealso::

         `DSGP 1 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-001.md>`_
           Read the DSGP that specifies the variable standards, and is used by
           this method.

   .. py:method:: execute_func(self, line)

      :param str line: A line of DiddiScript code.
      :raises diddiparser2.messages.error: If the execution fails.

      Execute a line with a function.

   .. py:method:: identify_value(self, arg, from_func=False)

      :param str arg: A string that must become a readable value for DiddiParser.
      :param bool from_func: This is used internally, to tell this method that the value was returned from a library/extension.

      Identify a value inside a text, and return the correct value.

      .. note::

         When ``from_func`` is True, the method won't fail if no values are found. Instead, it will return a string of the value.
         This is a workaround to one of our current issues with interpreting the values returned by libraries/extensions.

         However, this is not a recommended behavior. See `DiddiLeija/diddiparser2#43 <https://github.com/DiddiLeija/diddiparser2/issues/43>`_ for
         more information.

   .. py:method:: parse_string_indexing(self, line)

      :param str line: A string.

      Format a string with variables, using the DSGP 1 specification.

      .. seealso::

         `DSGP 1 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-001.md>`_
           Read the DSGP that specifies the variable indexing with strings,
           and is used by this method.

   .. py:method:: runfile(self)

      Runs :py:meth:`diddiparser2.parser.DiddiParser.executeline` for each line, and
      then prints a success message.

   .. py:method: print_command(self, cmd)

      :param str cmd: A formatted command.

      Prints the command as fancy as possible. By default, it
      only runs :py:func:`diddiparser2.messages.show_command`.

.. py:class:: InteractiveDiddiParser(DiddiParser)

   This is a subclass of :py:class:`diddiparser2.parser.DiddiParser`, which
   generates an interactive console to execute commands on real time. It
   left unchanged the methods from his ancestor (it only modified the ``__init__``
   and ``print_command``). However, it added some other methods, described below.

   .. py:method:: loop(self)

      Generates a "DiddiScript console" which calls
      :py:meth:`diddiparser2.parser.DiddiParser.executeline` for each line
      of input.

.. py:module:: diddiparser2.messages

``diddiparser2.messages`` -- Tools for user/parser interactions
---------------------------------------------------------------

These functions are used by the parser (generated by ``diddiparser2.parser``)
to interact with you as the "interpreter". Also, you can use some of this
functions in your extensions.

.. py:exception:: error

   An exception (which is a direct subclass of ``Exception``) raised when
   a function decided to stop the program.

.. py:function:: run_error(msg)

   :raises error: at the end of the function.

   Prints a "run error" in red, and stop the executions. This
   function is used when something in the execution failed. In
   most of the cases, this function is used by libraries and extensions.

.. py:function:: compile_error(msg)

   :raises error: at the end of the function.

   This function prints a "compile error" in red, and stop
   all the executions. This is commonly raised by the parser
   when a syntax error appears, a missing function is called,
   etc.

.. py:function: show_command(cmd)

   Prints the command *cmd* on a fancy color.

.. py:function:: show_warning(msg)

   This function prints a warning in yellow. It does not
   stop the execution.

.. py:function:: success_message(msg=None)

   :param msg: An optional message. If it's None, a default message is used.

   This function is called by the parser to tell the user
   that the execution finished succesfully.

.. py:module:: diddiparser2.editor

``diddiparser2.editor`` -- The DiddiScript editor
-------------------------------------------------

In most of the cases, the API contained in this subpackage
is just used internally for the DiddiScript Editor.

The main configurations happen at ``diddiparser2.editor.main``,
and are imported by ``diddiparser2.editor.__main__`` to use it
via ``python -m diddiparser2.editor``.

.. seealso::

   :doc:`editor`
     A complete guide to the editor's GUI and options.

Here's a small description of each component of this subpackage:

``diddiparser2.editor.__init__``
  The init file. It only contains a docstring.

``diddiparser2.editor.__main__``
  This enables the use of ``python -m diddiparser2.editor``, to do the
  same than the ``diddiscript-editor`` command.

``diddiparser2.editor.formatter``
  This is the responsible of the "themes stuff". Here, the theme
  colorization is made, the themes are stored, and themes are loaded
  from JSON files.

``diddiparser2.editor.main``
  This is where the GUI building, setup, and running is done. It
  generates a ``DiddiScriptEditor`` class, which contains a functional
  editor with Tk.
