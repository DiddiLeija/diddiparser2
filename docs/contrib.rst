.. _contrib-guide:

Contributing to this project
============================

This document explains how can you contribute to:

* DiddiParser 2 (the Python package, which is the official DiddiScript parser)
* DiddiScript (language)
* This documentation

Report a bug or propose a new feature
-------------------------------------

We have `GitHub Issues <https://github.com/DiddiLeja/diddiparser2/issues>`_ enabled,
so you can report bugs and propose features on it. In many cases, it is better to
open an issue before submitting a pull request, so we can discuss your idea first.

.. note::

   Proposals to the DiddiScript *language* (not libraries) should
   be filed as a DSGP. Read more at :ref:`dsgp-guide`.

Contributions to the parser (DiddiParser 2)
-------------------------------------------

DiddiParser 2 (``diddiparser2``) is a Python package. As a Python package, it accepts
contributions in Python code. You can contribute with libraries, parser behaviors,
etc. Also, you can contribute to GitHub-specific stuff, and anything
else living on the repository.

Forking the GitHub repo
^^^^^^^^^^^^^^^^^^^^^^^

To get the GitHub repository for development, use Git to clone it:

::
    
    git clone https://github.com/DiddiLeija/diddiparser2.git

(Also, you can clone from your own fork on GitHub, or use the GitHub.com interface).

Set up Nox
^^^^^^^^^^

We use `Nox <https://nox.thea.codes>`_ in our GitHub CI. But you can also
use it on your local clone. If you have installed ``nox``, you can run
sessions on it. They are necessary for testing on a local clone.

Code style and linters
^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

We follow the Black code style in our codebase. Also, we run linters
(``isort``, ``flake8``) to keep the codebase as clean as possible.

To reformat your code, run:

::

    nox -s format

To run linters, run:

::

    nox -s lint

To test your code with a DiddiScript console and the
latest code:

::

    nox -s generate-console

Contributions to documentation
------------------------------

.. image:: https://readthedocs.org/projects/diddiparser2/badge/?version=latest
    :target: https://diddiparser2.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

We host our documentation using `ReadTheDocs <https://readthedocs.org>`_ and
`Sphinx <https://sphinx-doc.org>`_. We accept contributions to the documentation's
source code, and their related items.

.. _dsgp-guide:

DSGPs (DiddiScript Grammar Proposals)... The future of DiddiScript
==================================================================

Do you want to contribute to the DiddiScript grammar? **Read this section, it is for you**.

The DiddiScript grammar depends on a series of documents called **DSGPs**
(DiddiScript Grammar Proposals). On those documents, the future of DiddiScript
is being developed. You can write and propose one, and maybe you can improve the
DiddiScript language!

.. seealso::

    `DSGP 0 <https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-0.md>`_
      This DSGP describes the scheme that all the DSGPs should follow.

    `Tree of DSGPs <https://github.com/DiddiLeija/diddiparser2/tree/main/dsgp/>`_
      This tree contains the complete list of DSGPs.

    `Search in-progress DSGPs <https://github.com/DiddiLeija/diddiparser2/pulls?q=is%3Apr+is%3Aopen+label%3A%22diddiscript%3A+DSGP%22>`_
      Pull requests of DSGPs that aren't on the official list, and are not ready yet.
