.. _editor-guide:

The DiddiScript Editor Guide
============================

This editor, built with the Python standard tools ``tkinter``
and ``idlelib``, is a Tk app focused in the DiddiScript language.

Commands to activate the editor
-------------------------------

The easiest way is the ``diddiscript-editor`` command,
included with the DiddiParser 2 Python package.

Also, since it's included in the DiddiParser 2 package, it
can be called with Python, via ``python -m diddiparser2.editor``. See
:py:mod:`diddiparser2.editor` for related information.

On a clone of the `GitHub repository <https://github.com/DiddiLeija/diddiparser2>`_,
you can also run a Nox session for generating the editor with the
latest code, via the ``nox -s generate-editor`` command.

Design of the editor
--------------------

The editor is pretty simple: it is a text widget, with a
menu that provides all the necessary options (see their options
below).

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

**Settings**
  Modify settings to customize your experience.

  **Set verbosity**
    Decide to set verbosity or not.

    If set, the parser will behave on verbose mode.
    For example, it will echo the functions and notify
    other events.

  **Set suffix ignoring**
    Decide to set suffix ignoring or not.

    If set, the editor won't raise a warning if a file to
    open does not have the DiddiScript suffix (``*.diddi``).

**Themes**
  Modify the themes (see below for detailed reference).

  **Load themes from a JSON file**
    Load custom themes from a JSON file (see the
    "Load customized themes" section below). It will ask each
    time it finds a valid theme on the file. If you accept, the
    theme will be registered.

  **See all the themes**
    In a separate window, show all the themes and their information.

  **Set theme**
    This menu will display a child menu, with all the available
    themes to select and apply.

Themes
------

*New in version 1.2.0.*

You can customize the DiddiScript editor using themes. By default,
we have provided you these themes:

* Light DiddiScript: A simple light theme.

* Dark DiddiScript: A simple dark theme.

Load customized themes
^^^^^^^^^^^^^^^^^^^^^^

We support customized themes loaded from a JSON file. The
"Load themes from a JSON file" option from the editor will
let you select a JSON file, and try to load themes from it.

The format of the JSON, to be accepted, is a dictionary or
a list of dictionaries, where each dictionary represents a
"theme". The dictionaries should have this keys:

* ``name``: A text with the theme's name. It will be used everywhere.

* ``description``: An optional text with a description of the theme.
* ``background``: The color of the theme's background.
  Examples: ``red``, ``#cfd3d7``.

Here we have a few examples of accepted JSON files:

.. code-block:: json

    {
      "name" : "My theme",
      "description" : "A personal theme.",
      "background" : "#ffffff"
    }

.. code-block:: json

    [
      {
        "name" : "One theme",
        "background" : "whitesmoke"
      },
      {
        "name" : "Another theme",
        "description" : "A theme different to 'One theme'.",
        "background" : "black"
      }
    ]
