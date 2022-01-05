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

``--verbose`` / ``-v``
^^^^^^^^^^^^^^^^^^^^^^

::

    diddiparser2 some_file.diddi --verbose

Pass ``verbose=True`` to :py:meth:`diddiparser2.parser.DiddiParser.__init__`. The
parser will echo all the commands found in the file.

``--compile-only`` / ``-c``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    diddiparser2 some_file.diddi --compile-only

Pass ``compile_only=True`` to :py:meth:`diddiparser2.parser.DiddiParser.__init__`.
The parser will just run what is necessary, and will compile and identify potential
errors.

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

``diddiscript-editor`` -- DiddiScript integrated editor
-------------------------------------------------------

DiddiParser 2 has an integrated editor built with Tk (via the
``tkinter`` Python module) with special functionalities focused
on DiddiScript.

It can be activated via the ``diddiscript-editor`` command, or
using ``python -m diddiparser2.editor``.

See a detailed guide at :ref:`editor-guide`.
