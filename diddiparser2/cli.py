"CLI tool for DiddiParser 2."

import argparse

from diddiparser2.parser import DiddiParser
from diddiparser2.parser import __version__ as parser_version


def get_parser():
    parser = argparse.ArgumentParser(prog=__name__)
    parser.add_argument("-V", "--version", action="version", version=parser_version)
    parser.add_argument("file", nargs="?", metavar="FILE")
    parser.add_argument(
        "--ignore-suffix",
        default=False,
        action="store_true",
        dest="ignore_suffix",
        help="Ignore the suffix warnings from the parser.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        dest="verbose",
        help="Run the code on verbose mode.",
    )
    parser.add_argument(
        "-c",
        "--compile-only",
        default=False,
        action="store_true",
        dest="compile_only",
        help="Just compile the code, with minimal executions.",
    )
    return parser


def main():
    parser = get_parser()
    options = parser.parse_args()
    if not options.file:
        parser.error("No such 'file' specified to run")
    script = DiddiParser(
        options.file,
        ignore_suffix=options.ignore_suffix,
        verbose=options.verbose,
        compile_only=options.compile_only,
    )
    script.runfile()


if __name__ == "__main__":
    main()
