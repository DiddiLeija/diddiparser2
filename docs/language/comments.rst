.. lang-comments:

DiddiScript comments
====================

Like most of the languages, DiddiScript supports *inline comments*.
However, it does not support *block comments* (a single comment with multiple lines).
Comments are defined with a ``!#``.

.. note::

   DiddiParser used to support block comments. However, DiddiParser2
   removed this feature.

Usage
-----

Comments can have their own line:

::

    !# This comment uses the whole line
    some_function();

But they can also coexist with functions at the same line:

::

    some_function();  !# This is an inline comment!
