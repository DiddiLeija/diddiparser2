import nox


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
    Run black and isort on the codebase. It is
    known that both formatters can have conflicts,
    so try to run `nox -s lint` before commiting!
    """
    session.install("-r", "tests/requirements.txt")
    session.run("isort", ".")
    session.run("black", ".")
    session.log("To get sure both formatters are happy, run 'nox -s lint'.")


@nox.session(name="generate-console")
def generate_console(session):
    """
    Generate an uncompromising DiddiScript console,
    installed on the Nox's virtualenv and using the
    latest DiddiParser2 code. Use it for testing purposes
    only.
    """
    session.install("-e", ".")
    session.log("Generating a DiddiScript console...")
    session.run("diddiscript-console")
