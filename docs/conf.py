# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'designbuilder_schema'
copyright = '2024, Bartlomiej Tokarzewski'
author = 'Bartlomiej Tokarzewski'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


import os, sys
sys.path.insert(0, os.path.abspath('..'))
print(sys.path)

extensions = ['sphinx.ext.autodoc', 
              'sphinx.ext.coverage', 
              'sphinx.ext.napoleon',
              "sphinxcontrib.apidoc",
              "sphinxcontrib.autodoc_pydantic"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
