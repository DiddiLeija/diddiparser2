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
    "Run black on the codebase."
    session.install("-r", "tests/requirements.txt")
    session.install("-e", ".")
    session.run("isort", ".")
    session.run("black", ".")
