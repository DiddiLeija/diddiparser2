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
   
   `Issue #5 <https://github.com/DiddiLeija/diddiparser2/issues/5>`_
     The issue related to the ``load_extension`` function. It also provides
     a short guide to write a correct DiddiScript extension.

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

Extension files are loaded in a similar way to standard libraries. For example,
imagine a file ``extension.py`` with these contents:

.. code-block:: python

    # You can import some things from DiddiParser2
    # (excluding "parser" and "cli"):
    from diddiparser2.messages import show_warning

    DIDDISCRIPT_FUNCTIONS = ("my_func", "my_func2")
    
    def my_func(some_arg):
        "A simple function"
        print(f"You gave me '{some_arg}'.")
    
    def my_func2(arg):
        """
        This doesn't require args. However, we
        should provide it, or it won't be accessible.
        We can warn if somebody gives an arg, if we
        want. That's your choice.
        """
        if len(arg) > 0:
            show_warning("We don't want args here!")
        print("I don't need args, I can stand by myself!")

Your file should have two requirements:

#. A ``DIDDISCRIPT_FUNCTIONS`` variable, which is taken by
   the parser to find the functions.
#. Each function should have *one positional argument*. If
   there are more or less arguments, the function won't be
   accessible by DiddiScript.

Then, in the DiddiScript file, you can run:

::

    load_extension("extension.py");
    
    my_func("something");
    my_func2();

That way, you can extend the DiddiScript powers!
