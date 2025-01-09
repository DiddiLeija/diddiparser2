.. _lib-builtin:

``_builtin`` -- Convenience functions
=====================================

*Added in 1.1.0*.

This special module is loaded on the parser's initialization.

.. note::

    *Since version 1.1.0*, this module replaces the :ref:`tool-functions`.
    Also, it is now the module where ``MODULE_FUNCTIONS`` is stored.

Contents
--------

Replacements for the *tool functions*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At version 1.0.0, we used to have something called *tool functions*,
a bunch of static "functions" that were available everywhere, anytime.
But since version 1.1.0, we decided to move those functions into this
library. That way, you can both replace these functions with functions
from other libraries, and load them again by loading ``_builtin``.

.. py:function:: cd(arg)
                chdir(arg)

   :param arg: The path where to move.

   Change the current working directory to *arg*. It returns a :ref:`type-text`
   of the new current working directory.

.. py:function:: print_available_functions(arg)

   :param arg: A mandatory argument. This function won't use it at all.

   Print the available functions, and their origin.

.. _lang-modules:

.. py:function:: load_module(*args)

   :param args: An undefined number of text values to load.

   This loads a library from ``diddiparser2.lib``, and all their
   contents. It loads as many libraries as you request.

.. _lang-extensions:

.. py:function:: load_extension(*args)

   :param args: An undefined number of text values to load.

   This will load an extension. An extension is a Python file that
   can be imported from the current working directory.
   This function loads as many libraries as you request.

   .. note::

      If the "extensions file" directory is not listed by default
      on :py:data:`sys.path`, use the :py:func:`add_extensions_location`
      function first (see below).

   .. seealso::

       `DSGP 3 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-003.md>`_
         The DSGP that provides a guide for extensions.

Stuff loaded from the ``simpleio`` library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following functions are taken from the ``simpleio``
library. The reference for the original functions can be
found at :doc:`simpleio`.

.. py:function:: print_text(arg)

   A shortcut for ``simpleio.print_text``.

.. py:function:: print_line(arg)

   A shortcut for ``simpleio.print_line``.

.. py:function:: store_input(arg)

   A shortcut for ``simpleio.store_input``.

.. py:function:: warning(arg)

   A shortcut for ``simpleio.warning``.

.. py:function:: err(msg)

   A shortcut for ``simpleio.err``.

Other functions
^^^^^^^^^^^^^^^

.. py:function:: add_extensions_location(arg)

   :param arg: A text-like path.

   This function extends :py:func:`sys.path`, enabling more
   locations to export extensions. It should be used before
   :py:func:`load_extension`, in case the "extensions file"
   is not included in :py:func:`sys.path`.
