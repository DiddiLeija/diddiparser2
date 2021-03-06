.. _lib-guide:

Standard DiddiScript libraries
==============================

.. toctree::
   :hidden:
   
   _builtin
   fileio
   math
   simpleio
   sqlite
   subprocessing

These libraries are stored by DiddiParser 2 (at ``diddiparser2.lib``) and
are accessible on DiddiScript via the ``load_module`` function:

::

    load_module("some_library");

    function_from_library("...");

.. seealso::

   `Tree of DiddiScript libraries <https://github.com/DiddiLeija/diddiparser2/tree/main/diddiparser2/lib>`_
     See the source code of the current DiddiScript libraries.
