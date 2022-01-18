.. _lang-extensions:

Extending the DiddiScript library via ``load_extension``
======================================================

In addition to the standard library, DiddiScript can load
custom functions, called *extensions*. They can be loaded
with the special ``load_extension`` function.

.. seealso::

   :ref:`lang-modules`
     Refer to this function for loading standard DiddiScript
     libraries.

   `DSGP 3 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-003.md>`_
     This DSGP provides the ultimate guide to write useful extensions.

.. _load-extension-function:

Usage of ``load_extension``
---------------------------

::

    !# A Python file/module that is in the same directory than us
    load_extension("my_extension");

    !# A Python module that lives in a package
    load_extension("some_pkg.my_extension");

The ``load_extension`` can load functions from Python files, like a
standard module. The whole string is interpreted to be passed to an
import statement and the contents are loaded.

The extension file
------------------

Refer to
`DSGP 3 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-003.md>`_
for guidance about writing a DiddiScript extension.
