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
copyright = "2021, Diego Ramirez"

# HTML specs
html_theme = "furo"
