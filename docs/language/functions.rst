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

.. seealso::

   :ref:`lang-modules`
     A detailed description of ``load_module``.

   :ref:`lang-extensions`
     A detailed description of ``load_extension``.
