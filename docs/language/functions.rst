.. _lang-functions:

Functions
=========

DiddiScript can handle functions with one argument, or without arguments.

Usage without arguments
-----------------------

::

     !# A function without arguments
     some_function();

     !# This function has no "arguments", if
     !# that is supported by the function
     some_function("");

     !# But this one has arguments. At least,
     !# that is what DiddiParser thinks...
     some_function(" ");

If the function does not need arguments, you can just use
an empty function. Also, an empty text (`""`) is interpreted
like a "missing argument".

.. note::

   DiddiParser2 standard functions will warn you if you added an
   argument to a function that doesn't need arguments. However, it won't
   raise an error -- it will just ignore the argument.

   Also, you can tell your custom functions (loaded as extensions) to
   warn if they don't need arguments.

Usage with arguments
--------------------

::

    !# The text is interpreted as an argument
    some_function("some argument");

    !# However, the argument below is interpreted
    !# like exactly the same.
    some_function(some argument);

In most of the cases, the functions need one argument. They can
be quoted ("") or not (DiddiParser will treat them as the same).

.. _tool-functions:

Special functions *(tool functions)*
------------------------------------

We have saved special functions, to handle and load DiddiScript
stuff.

.. warning::

   If you load or create a function that replaces one of the special functions
   listed here, you will probably harm the functionality of the parser, because
   the original functions will be overwritten.

``cd(path)`` | ``chdir(path)``
  Change the current working directory (*cwd*), if possible.

``load_module(module)``
  This function loads functions from the DiddiScript standard
  library, for its usage on the code. If a new function has the
  same name than an existing function, the old function will be
  overwritten and replaced by the new one.

``load_extension(extension)``
  This function loads functions from a custom Python file. Its
  rules are the same than those related to ``load_module``, with a
  few other specific rules.

``print_available_functions()``
  This function prints both the special functions and the loaded
  libraries.

``store_last_value(variable)``
  Store the last value returned by a function (or Null) on the variable
  *variable* (with quoted name).

.. seealso::

   :ref:`lang-modules`
     A detailed description of ``load_module``.

   :ref:`lang-extensions`
     A detailed description of ``load_extension``.
