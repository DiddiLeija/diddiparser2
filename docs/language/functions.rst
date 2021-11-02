Functions
=========

DiddiScript can handle functions with one argument, or without arguments.

..note::

  DiddiParser2 will warn you if you added an argument to a function that
  doesn't need arguments. However, it won't raise an error -- it will
  just ignore the argument.

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
