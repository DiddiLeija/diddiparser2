.. _lang-modules:

Loading DiddiScript libraries via ``load_module``
=================================================

The DiddiScript libraries provide several solutions as functions. There is a standard library
of DiddiScript functions, that can be easily loaded and used.

.. seealso::

   :ref:`lib-guide`
     A detailed reference to the DiddiScript standard library.

.. _load-module-function:

Usage of ``load_module``
------------------------

``load_module`` is a special function that load functions from the standard library. It looks for
the name provided inside ``diddiparser2.lib``. Then, all their functions will be available.

::

    !# Load the "simpleio" library
    load_module("simpleio");
    
    !# Now we can call a function
    !# defined in "simpleio":
    print_text("Hello world!");
