.. _quickstart-tutorial:

DiddiParser 2 tutorial
======================

This document will help you learn to start with DiddiScript
and DiddiParser 2.

Install DiddiParser 2
---------------------

To use DiddiScript, you should install its parser, DiddiParser 2. You can get it
using `Pip <https://pip.pypa.io>`_:

::

    pip install diddiparser2

To upgrade it:

::

    pip install --upgrade diddiparser2

Write your DiddiScript file
---------------------------

First of all, you need to write a DiddiScript file (``*.diddi``). You can define instructions
that run fast with this language.

You can store data using variables:

::

    var my_var;              !# Null
    var x = 23.4;            !# Floating numbers
    var y = 56;              !# Integers
    var name = "Diego";      !# Text
    var is_true = False;     !# Booleans
    var empty_stuff = Null;  !# Null (explicitly)

Also, you can call functions, and pass arguments or not:

::

    function1(my_var);             !# You can pass variables
    function2(413);                !# Or values
    function3("My text", my_var);  !# You can pass several arguments
    function4();                   !# Or no arguments at all!

You can insert variables into text:

::

    var name = "Diego";
    var greeting = "Hello, ${name}!";  !# This would become "Hello, Diego!"

Also, there is a bunch of special functions, that conform your toolbox. To see
them, run this:

::

    print_available_functions();     !# Print all the available functions

You can use pre-loaded functions, and use other functions:

::

    !# The functions below were loaded by default
    store_input("Name: ");
    !# The special '_memory' represents the last value. In this case, the obtained input:
    print_line("Hello, ${_memory}. I am DiddiScript");

    load_module("math");  !# This will load the 'math' library

    !# Something added by 'math'
    sum_operation(1, 1);  !# 1 + 1

    print_line("1 + 1: ${_memory}");

Execute your file
-----------------

After you wrote and saved your file, you can run the ``diddiparser2`` command:

::

    diddiparser2 my_diddiscript_file.diddi

(Also, using ``python -m diddipase2`` works fine).

And the inputs/outputs will be shown!

::

    $ diddiparser2 my_diddiscript_file.diddi
    Name: Diego
    Hello, Diego. I am DiddiScript.
    1 + 1: 2

Lower-level usage
^^^^^^^^^^^^^^^^^

Since it is written in Python, DiddiParser 2 can be used under Python code!

.. code-block:: python

    # These lines of code are equivalent to
    # running "diddiparser2 my_diddiscript_file.diddi"
    from diddiparser2.parser import DiddiParser

    script = DiddiParser("my_diddiscript_file.diddi")
    script.runfile()

The interactive console
-----------------------

If you don't want to write a DiddiScript file, you can try commands in real time using the DiddiScript interactive console (or REPL).
You can call it via the ``diddiscript-console`` command:

::

    $ diddiscript-console
    Welcome to the interactive DiddiParser console.
    Parser version: 1.0.0
    ============================================================

    > !# put your commands here!

Going deeper
------------

**You know the DiddiScript basics! Hooray!**

But if you want to learn more, you can read more in this documentation:

* **Do you want to master the DiddiScript language?** Read :doc:`language/index`.
* **Do you want to learn the parser internals, or how to use the CLI?** Dive into :doc:`cli` or :doc:`reference`.
* **Are you interested in the future of the project?** Go to :doc:`contrib`.
