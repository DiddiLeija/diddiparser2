# Sphinx config file.
import os
import sys

try:
    import importlib.metadata as metadata
except ImportError:
    import importlib_metadata as metadata

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("."))

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

version = metadata.version("diddiparser2")
release = version

# HTML specs
html_theme = "furo"
