# Sphinx config file.

# we want some extensions, so we are including them here:
extensions = [
    # first-party
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    # third-party
    "sphinx_copybutton",
]

language = "en"
project = "DiddiParser2"
author = "Diego Ramirez"
copyright = "2021-present, Diego Ramirez"

# TODO: We should fix this to display the versions.
#       See https://github.com/DiddiLeija/diddiparser2/pull/62
#       for the background of the issue.
#
# version = pkg_version
# release = version

# HTML specs
html_theme = "furo"
