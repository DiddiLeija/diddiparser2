.. _editor-guide:

The DiddiScript Editor Guide
============================

This editor, built with the Python tools ``tkinter``
and ``idlelib``, is a Tk app focused in the DiddiScript
language.

Commands to activate the editor
-------------------------------

The easiest way is the ``diddiscript-editor`` command,
included in the DiddiParser 2 Python package.

Also, since it's included in the DiddiParser 2 package, it
can be called with ``python -m diddiparser2.editor``. See
:py:mod:`diddiparser2.editor` for related information.

On a clone of the `GitHub repository <https://github.com/DiddiLeija/diddiparser2>`_,
you can also run a Nox session for generating the editor with the
latest code, via the ``nox -s generate-editor`` command.

Design of the editor
--------------------

The editor is pretty simple: it is a text widget, with a
menu that provides all the necessary options (see below).

Editor's options and tools
--------------------------

A quick guide to the options of the editor's menu.

**About...**
  Display useful information as separate windows.

  **About DiddiScript**
    A quick introduction to DiddiScript. It is the main docstring
    of ``diddiparser2``.

  **About DiddiParser 2**
    Information about the DiddiScript parser. It is the docstring
    of :py:mod:`diddiparser2.parser`.

  **About this editor**
    Information about the DiddiScript editor.

**File**
  Modify or manage the file stuff.

  **Save As...**
    Open a "Save As" dialog, and save the current contents.

  **Save**
    If you're already on a file, save without asking. If not,
    do the same than the Save As function.

  **Open...**
    Open an existing file.

**Run**
  Run DiddiScript stuff. Logs are shown in console.

  **Compile code**
    Run the DiddiScript code in "compile only" mode.

  **Run code**
    Run the DiddiScript code.