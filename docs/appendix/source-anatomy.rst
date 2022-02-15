.. _anatomy:

Appendix: Anatomy of the source code
====================================

This small document explains the anatomy of the DiddiParser 2 source
code, that can be found at `GitHub <https://github.com/DiddiLeija/diddiparser2>`_.

* ``.github/``: Where the GitHub-related stuff is stored. The bots we use are configurated in this folder.

  * ``ISSUE_TEMPLATE/``: The issue templates and their config file are here.
  
  * ``workflows/``: The GitHub actions are configured here.

* ``diddiparser2/``: The DiddiParser2 package.

  * ``editor/``: This subpackage is the responsible of the DiddiScript editor.
  
    * ``__init__.py``
    
    * ``__main.py__``: The file that enables ``python -m diddiparser2.editor``.
    * ``formatter.py``: This file operates the editor themes.
    * ``main.py``: The generation file of the editor GUI. It is also the responsible of the compile/run logics of the editor.
  
  * ``lib/``: All the standard libraries are here, including ``_builtin``.
  
  * ``__init__.py``: This is the init file. It activates Colorama (which is used to colorize the execution)
    and defines a ``__version__`` (which is, actually, ``diddiparser2.parser.__version__``).
  * ``__main__.py``: This file enables the use of ``python -m diddiparser2``, the DiddiParser2 main CLI.
  * ``cli.py``: The place where the main CLI is set.
  * ``diddiscript_types.py``: The main factory of the DiddiScript types, represented by Python classes.
  * ``messages.py``: The factory of the parser's messages, like successes, warnings and errors.
  * ``parser.py``: The main parser. It also manipulates the DiddiScript interactive console.

* ``docs/``: All the documentation lives here. We won't discuss each component now, but we'll mention the main folders.
  
  * ``appendix/``: A small appendix of handy references.
  * ``language/``: The DiddiScript language reference.
    
    * ``stdlib/``: The reference for the standard libraries.
  
  * ``conf.py``: The Python file that sets up Sphinx for building the docs.

* ``dsgp/``: The DSGPs (DiddiScript Enhancement Proposals) are stored here. We won't mention each one of them now.

* ``tests/``: The DiddiScript tests are here. They are not Pytest tests (not by now), they are DiddiScript files.
  
  * ``requirements.txt``: These are the requirements for running tests and linters.

* ``.gitignore``

* ``CHANGELOG.md``: The changelog per version.
* ``CONTRIBUTING.md``: A really basic contributor guidelines. It actually points to the contributor reference in the docs.
* ``LICENSE.txt``: Our license file, which is the MIT License.
* ``README.md``: The main README file, which is used in the GitHub repo and the PyPI page.
* ``noxfile.py``: Our setup file for Nox, which runs our automation.
* ``pyproject.toml``: It only defines the build system (setuptools), the metadata is defined in ``setup.cfg``.
* ``release-requirements.txt``: The requirements for building a release.
* ``setup.cfg``: The file where the metadata is stored.
