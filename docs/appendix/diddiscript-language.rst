Appendix: DiddiScript (language)
================================

.. note::

   This was moved here from the old wiki from the GitHub repository.

The **DiddiScript** language is an extensible, on-development programming language. Its goal is create a language
that becomes the bridge between other well-stablished languages, using a simple syntax.

History
-------

DiddiParser 1 (May 2021 -- September 2021)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`DiddiParser <https://github.com/DiddiLeija/diddiparser>`_ (or also called DiddiParser 1, because of its successor)
was the first DiddiScript parser, written in Python and created by `Diego Ramirez <https://diddileija.github.io>`_.
On May 14, 2021, the first release of the parser (`1.0.0 <https://pypi.org/project/diddiparser/1.0.0/>`_) was released.
Then, some minor releases were published. However, due to several parser issues, the project was abandoned at
September 2nd, 2021, one day after the 1.3 release.

This parser defined a really simple syntax for DiddiScript, with only functions and comments:

::

    !# Inline comment

    /*
    Block comments were accepted, but
    they became a little glitchy
    */

    some_function();

It had a very limited standard library, and it was hard to extend (via a rough ``diddi_extensions.py`` file per directory).

DiddiParser 2 (November 2021 -- today)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the death of DiddiParser 1, the author of that package wasn't sure if he could restore his forgotten language.
The old parser could not be fixed and just released, but a new package was going to take the idea of DiddiScript again.

At November 3, 2021, Ramirez started to develop a new parser, called `DiddiParser 2 <https://github.com/DiddiLeija/diddiparser2>`_
(in honor to the previous parser). The goal was to take and improve elements from the old parser, with a more extensible library,
and more flexible extensions (any Python file would become an extension).

Also, this parser introduced the **DSGPs** (DiddiScript Enhancement Proposals) to ease the syntax development.
For example, the DSGP 1 introduced variables and text indexing to DiddiScript:

::

    var name = "Diego";
    some_function("Hi! I am ${name}."); !# Equivalent to "Hi! I am Diego."

Other DSGPs contributed to build a higher-level language.

Finally, at January 9th, 2022 (after 3 months of early development), the first release (`1.0.0 <https://pypi.org/project/diddiparser2/1.0.0/>`_)
was released to PyPI. At the `1.1.0 <https://pypi.org/project/diddiparser2/1.1.0/>`_ release (to be more precise, the
`1.1.0.post1 <https://pypi.org/project/diddiparser2/1.1.0.post1/>`_ release), the parser made its first major refactoring: it finally dropped the
"functions with a single argument" syntax, and enabled infinite arguments and direct usage of variables and values.

For the 2.x releases, there're plans to refactor the syntax again to make it more advanced.
