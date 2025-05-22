from __future__ import annotations

import os
from pathlib import Path


from sphinx_gallery.sorting import FileNameSortKey
import cmake_detection



project = "cmake_detection"
author = "Louis Pujol"
version = cmake_detection.__version__


# mathjax config to properly display math in docs
mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"]],
        "displayMath": [["\\[", "\\]"]],
    }
}

extensions = [
    # 'sphinx_tabs.tabs',
    "sphinx_design",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "numpydoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
    "sphinx_math_dollar",
]

source_suffix = [".rst"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

sphinx_tabs_valid_builders = ["linkcheck"]
html_theme = "furo"
myst_enable_extensions = ["colon_fence", "linkify"]

sphinx_gallery_conf = {
    "examples_dirs": "../examples/",  # path to your example scripts
    "gallery_dirs": "auto_examples",  # path to where to save gallery generated output
    "first_notebook_cell": "%matplotlib inline",
    "reset_modules_order": "both",
    "within_subsection_order": FileNameSortKey,
    "image_scrapers":  ("matplotlib",),
}



