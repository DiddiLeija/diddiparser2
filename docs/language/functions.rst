.. _lang-functions:

Functions
=========

DiddiScript can handle functions with one argument, or without arguments.

Usage without arguments
-----------------------

::

     !# A function without arguments
     some_function();

If the function does not need arguments, you can just use
the function without arguments.

.. note::

   DiddiParser2 standard functions will warn you if you added an
   argument to a function that doesn't need arguments. However, it won't
   raise an error -- it will just ignore the argument.

   Also, you can tell your custom functions (loaded as extensions) to
   warn if they don't need arguments.

Usage with arguments
--------------------

::

    !# Use as many arguments you need
    some_function("arg 1", arg2);

In most of the cases, the functions need one argument. They can
be values or variables.

.. _tool-functions:

Special functions *(tool functions)*
------------------------------------

This has moved into :doc:`stdlib/builtin`.
