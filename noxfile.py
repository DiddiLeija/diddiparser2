import os
import time

import nox

nox.options.sessions = ["format-and-lint"]


@nox.session
def lint(session):
    "Run linters."
    session.install("-r", "tests/requirements.txt")
    session.install("-e", ".")
    session.run("flake8", ".", "--count", "--show-source", "--statistic")
    session.run("isort", ".", "--check-only", "-v")
    session.run("black", "--check", ".")


@nox.session
def format(session):
    """
    Run black and isort on the codebase.
    It is known that both formatters can have conflicts,
    so try to run `nox -s lint` before commiting!
    """
    session.install("-r", "tests/requirements.txt")
    session.run("isort", ".")
    session.run("black", ".")


@nox.session(name="format-and-lint")
def format_and_lint(session):
    """
    Run both formatters and linters.
    It should not fail, unless one of the
    linters have a conflict with another
    linter.
    """
    session.log("Running formatters...")
    session.install("--upgrade", "nox")
    session.log("Formatting...")
    session.run("nox", "-s", "format")
    session.log("Running linters...")
    session.run("nox", "-s", "lint")
    session.log("It seems like everything succeeded!")


@nox.session
def tests(session):
    "Test the DiddiScript features, using our own strategy."
    session.install("-r", "tests/requirements.txt")
    session.install("-e", ".")
    session.log("Starting tests. See the logs to analyze.")
    for file in os.listdir("tests"):
        if file.endswith(".diddi"):
            session.run("diddiparser2", f"tests/{file}")
            time.sleep(1)


@nox.session(name="generate-console")
def generate_console(session):
    """
    Generate an uncompromising DiddiScript console.
    It is installed on the Nox's virtualenv and using the
    latest DiddiParser2 code. Use it for testing purposes
    only.
    """
    session.install("-e", ".")
    session.log("Generating a DiddiScript console...")
    session.run("diddiscript-console")


@nox.session(name="generate-editor")
def generate_editor(session):
    """
    Generate a DiddiScript editor with the latest code.
    It is installed on the Nox's virtualenv and uses the
    latest DiddiParser2 code. Use it for testing purposes
    only.
    """
    session.install("-e", ".")
    session.log("Opening the editor...")
    session.run("diddiscript-editor")


@nox.session
def release(session):
    """
    Just for maintainers: cut a release and publish to PyPI
    using Setuptools, Wheel and Twine.
    """
    # install deps
    session.install("-r", "release-requirements.txt")
    # install the source on editable mode to catch a "build error"
    # before publishing
    session.log("Installing on the virtualenv to test compatibility...")
    session.install("-e", ".")
    # if this hasn't failed, we can just go ahead and
    # build the distributions, and then release
    session.log("Done. Now, we will cut and publish a release...")
    session.run("setup.py", "sdist", "bdist_wheel")
    session.run("python", "-m", "twine", "upload", "dist/*")
