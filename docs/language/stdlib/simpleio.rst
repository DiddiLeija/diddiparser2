``simpleio`` -- Common I/O interactions
=======================================

This library provides basic user/machine
interactions. It helps to work with 3 kind of
streams:

* Input
* Output
* Errors

It also enables the usage of input storage, for its usage
on the output stream.

Functions
---------

.. py:function:: program_exit(msg)

   :param msg: The message to exit, or an exit code.

   Exit with a message, or an exit code. That way, you can
   exit by yourself.

.. py:function:: print_text(txt)

   :param txt: The text to be printed on the screen.

   Print a simple text on the screen.

.. py:function:: store_input(msg)

   :param msg: The message to prompt the input.

   Store an input, prompted with message *msg*. The input
   will keep safe until requested.

.. py:function:: print_input()

   Just print the stored input, when available. This function
   doesn't require arguments.

   .. note::

      If there is no stored text, and this function is called,
      a run error will be raised.
