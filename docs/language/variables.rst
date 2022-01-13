.. _lang-variables:

DiddiScript variables
=====================

Variables help us to store and use data. You can use it on functions,
or by their own. This document explains how to define and use them on
your DiddiScript code.

.. seealso::

   `DSGP 1 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-1.md>`_
     Read the DSGP that specifies the variable standards, and the concept of
     DiddiScript variables.

Definition syntax
-----------------

::

    var x;
    var x = "Hello, world!";

To define a variable, type the keyword ``var``, then the variable name. If
you want to preset the value, type ``=`` and then a valid value to store. If you
don't preset a value, a default :ref:`type-null` will be stored.

Usage inside text (indexing)
----------------------------

You can insert variables to text. Use the ``${variable_name}``
syntax on your text to insert variables on them:

::

    var name = "Diego";
    var greeting = "Hello, ${name}!";

Reserved variables
------------------

We have reserved a few variable names for some operations. They cannot be modified,
but you can use them for getting certain data.

``_memory``
^^^^^^^^^^^

*Introduced in 1.1.0.*

This special variable replaces the old function ``store_last_value()``. At the
beginning of the execution, it is completely forbidden. But under some events, it
stores values for it's further usage.

When a variable is created, ``_memory`` becomes the variable content
generated at that time.

When a function is called, and it returns something, ``_memory`` becomes that
return value.

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
