import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

GREEN = '\033[92m'
END_GREEN = '\033[0m'

print(f"{GREEN}[INFO] sys.path:{END_GREEN} {sys.path}")

src_path = os.path.abspath('../src')
print(f"{GREEN}[INFO] Contenu du répertoire src :{END_GREEN} {os.listdir(src_path)}")

notebook_path = os.path.join(src_path, 'JsonMerger.ipynb')
print(f"{GREEN}[INFO] Existe-t-il ?{END_GREEN} {os.path.exists(notebook_path)}")


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ImmunoGit'
copyright = '2025, SDG'
author = 'SDG'
release = '0.1-dev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
]

nbsphinx_allow_errors = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

nbsphinx_execute = 'never'
