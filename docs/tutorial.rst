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

First of all, you need to write a DiddiScript file (``*.diddi``). You can define variables
and run functions fastly with this language.

The most common thing in DiddiScript are functions:

::

    some_function();

Functions can take arguments. Actually, many of them need arguments. They always go quoted:

::

    some_function("some arg");

You can add comments everywhere:

::

    !# This comment is a whole line
    
    some_function();  !# This is an inline comment

We have a bunch of special functions, that are available by default:

::

    load_module("some library");     !# Load a standard DiddiScript library
    load_extension("my extension");  !# Load a Python file that contains DiddiScript stuff
    chdir("my_folder");              !# Move the current working directory
    print_available_functions();     !# Print all the available functions
    store_last_value("some_var");    !# If a function returned something, store the value inside "my_var"

Also, it is possible to define variables, and you can insert their contents into function arguments:

::

    !# "simpleio" is the most common DiddiScript library. It
    !# is useful for interacting with the user.
    load_module("simpleio");
    
    var name;  !# For now, keep "name" empty
    
    store_input("Name: ");  !# Ask for a name
    store_last_value("name");  !# Store the last value (in this case, whatever returned by store_input) into "name"
    print_text("Hello, ${name}. I am DiddiScript.");  !# Replace "${name}" with the true value of "name"

Execute your file
-----------------

After you wrote and saved your file, you can run the ``diddiparser2`` command:

::

    diddiparser2 my_diddiscript_file.diddi

(Also, using ``python -m diddipase2`` works fine).

And the inputs/outputs will be shown!

::

    $ cat my_diddiscript_file.diddi
    !# "simpleio" is the most common DiddiScript library. It
    !# is useful for interacting with the user.
    load_module("simpleio");
    
    var name;  !# For now, keep "name" empty
    
    store_input("Name: ");  !# Ask for a name
    store_last_value("name");  !# Store the last value (in this case, whatever returned by store_input) into "name"
    print_text("Hello, ${name}. I am DiddiScript.");  !# Replace "${name}" with the true value of "name"
    
    $ diddiparser2 my_diddiscript_file.diddi
    Name: Diego
    Hello, Diego. I am DiddiScript.

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

* **Do you want to master the DiddiScript language?** Read :ref:`lang-guide`.
* **Do you want to learn the parser internals, or how to use the CLI?** Dive into :ref:`cli-guide` or :ref:`api-reference`.
* **Are you interested in the future of the project?** Go to :ref:`contrib-guide`.
