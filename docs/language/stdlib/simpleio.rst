.. _lib-simpleio:

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

   Print a simple text on the screen, without adding a newline.

.. py:function:: print_line(txt)

   :param txt: The text to be printed on the screen.

   Print a simple text on the screen, with adding a newline.

.. py:function:: store_input(msg)

   :param msg: The message to prompt the input.

   Store an input, prompted with message *msg*. The input
   will keep safe until requested, or called for storage in
   a variable.

.. py:function:: warning(msg)

   :param msg: The message to show.

   Shows a warning using
   :py:function:`diddiparser2.messages.show_warning`.
