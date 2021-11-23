.. _lang-variables:

DiddiScript variables
=====================

.. seealso:
   `DSGP 1 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-1.md>`_
     Read the DSGP that specifies the variable standards, and the concept of
     DiddiScript variables.

Variables help us to store and use data. You can use it on functions,
or by their own. This document explains how to define and use them on
your DiddiScript code.

Definition syntax
-----------------

::

    var x;
    var x = "Hello, world!";

To define a variable, type the keyword ``var``, then the variable name. If
you want to preset the value, type ``=`` and then a valid value to store. If you
don't preset a value, a default :ref:`type-null` will be stored.

Usage under functions (indexing)
--------------------------------

You can replace text with variables on functions. Use the ``${variable_name}``
syntax on your argument to insert variables on them:

::

    var name = "my name";
    var age = 20;

    say_hello("Hello, ${name}");
    find_age("${age}"); !# NOTE: even this is necessary!

.. _variable-types-guide:

List of allowed types
---------------------

.. _type-null:

Null
^^^^

An "empty value", equivalent to the Python ``None`` and the C ``null`` types.

.. _type-text:

Text
^^^^

A string of Unicode (most of the times UTF-8 encoded) characters.
They go quoted (with ``""`` or ``''``) in most of the code.

.. _type-bool:

Booleans
^^^^^^^^

``True`` or ``False``.

.. _type-floating:

Floating numbers
^^^^^^^^^^^^^^^^

Decimal numbers, like ``12.34``.

.. _type-integer:

Integers
^^^^^^^^

Natural numbers like ``123``.
