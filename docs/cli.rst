Command-line usage
==================

The DiddiParser 2 command-line tool can be accessed by 2 ways: by running
the traditional ``python -m diddiparser2`` or the ``diddiparser2`` console
script:

::

    python -m diddiparser2 file.diddi
    diddiparser2 file.diddi


Options
-------

``--version``
^^^^^^^^^^^^^

::

    diddiparser2 --version

Print the parser version.

``--ignore-suffix``
^^^^^^^^^^^^^^^^^^^

::

    diddiparser2 --ignore-suffix other_script.txt

Ignore the warnings caused when the script does not end with the standard
``.diddi`` prefix.
