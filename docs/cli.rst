.. _cli-guide:

Command-line usage
==================

The DiddiParser 2 command-line tool can be accessed by 2 ways: by running
the traditional ``python -m diddiparser2`` or the ``diddiparser2`` console
script:

::

    python -m diddiparser2 file.diddi
    diddiparser2 file.diddi


``diddiparser2`` options
------------------------

``--version``
^^^^^^^^^^^^^

::

    diddiparser2 --version

Print the parser's version.

``--ignore-suffix``
^^^^^^^^^^^^^^^^^^^

::

    diddiparser2 other_script.txt --ignore-suffix

Ignore the warnings caused when the script does not end with the standard
``.diddi`` prefix. This passes ``ignore_suffix=True`` to
:py:meth:`diddiparser2.parser.DiddiParser.__init__`.

``--verbose``
^^^^^^^^^^^^^

::

    diddiparser2 some_file.diddi --verbose

Pass ``verbose=True`` to :py:meth:`diddiparser2.parser.DiddiParser.__init__`. The
parser will echo all the commands found in the file.

``diddiscript-console`` -- Interactive console
----------------------------------------------

DiddiParser 2 has provided an interactive console to run command-by-command
(which is, formally, a REPL), via the ``diddiscript-console`` command:

::

    C:> diddiscript-console

    Welcome to the interactive DiddiParser console.
    Parser version: 1.0.0
    ============================================================

    >
