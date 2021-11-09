.. _lib-fileio:

``fileio`` -- Regular file interactions
======================================

This library provides functions to interact
with real files in the system.

Functions
---------

.. py:function:: printfile(path)

   :param path: The selected path.

   This function tries to open the *path*, and then print it
   on the console.

.. py:function:: ensurefile(path)

   :param path: The path to find.

   Verify if a file is accessible, and print the results.

.. py:function:: store_file(path)

   :param path: The existing file to store.

   Open and read a real file, then store its contents
   on the library for its usage.

.. py:function:: print_stored()

   Print the file that lives in the library memory. If
   nothing is there, raise a run error.
