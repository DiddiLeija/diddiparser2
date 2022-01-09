"""
DiddiScript is a programming language that can
handle functions and variables.

Its parser, DiddiParser 2, is written in Python,
and is available in most of the environments.
"""

from colorama import init

from diddiparser2.parser import __version__ as parser_version

__version__ = parser_version

init(autoreset=True)
