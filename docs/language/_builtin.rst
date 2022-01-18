.. _lib-builtin:

``_builtin`` -- Convenience functions
=====================================

This special module is loaded on the parser's initialization.

*Since version 1.1.0, this replaces the tool functions. Also, it is now
the module where ``MODULE_FUNCTIONS`` is stored.*

Contents
--------

.. py:func:: cd(arg)
             chdir(arg)

   :param arg: The path where to move.

   Change the current working directory to *arg*.

.. py:func:: print_available_functions(arg)

   :param arg: A mandatory argument. This function won't use it at all.

   Print the available functions.

.. _lang-modules:

.. py:func:: load_module(*args)

   :param args: An undefined number of text values to load.

   This loads a library from ``diddiparser2.lib``, and all their
   contents. It loads as many libraries as you request.

.. _lang-extensions:

.. py:func:: load_extension(*args)

   :param args: An undefined number of text values to load.

   This will load an extension. An extension is a Python file that
   can be imported from the current working directory.
   This function loads as many libraries as you request.

   .. seealso::

       `DSGP 3 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-003.md>`
         The DSGP that provides a guide for extensions.

.. py:func:: print_text(arg)

   A shortcut for ``simpleio.print_text``. See its reference
   `here <https://diddiparser2.readthedocs.io/en/latest/language/stdlib/simpleio.html#print_text>`_.

.. py:func:: print_line(arg)

   A shortcut for ``simpleio.print_line``. See its reference
   `here <https://diddiparser2.readthedocs.io/en/latest/language/stdlib/simpleio.html#print_line>`_.

.. py:func:: store_input(arg)

   A shortcut for ``simpleio.store_input``. See its reference
   `here <https://diddiparser2.readthedocs.io/en/latest/language/stdlib/simpleio.html#store_input>`_.
