import os
import sys

# paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)
docs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, docs_path)

# debug (run file to see output)
GREEN = '\033[92m'
END = '\033[0m'

print(f"{GREEN}[INFO] Current working dir :{END} {os.getcwd()}")
print(f"{GREEN}[INFO] sys.path :{END} {sys.path}")
print(f"{GREEN}[INFO] src content :{END} {os.listdir(src_path)}")

for root, dirs, files in os.walk(src_path):
    notebooks = [f for f in files if f.endswith('.ipynb')]
    if notebooks:
        print(f"{GREEN}[INFO] Notebooks found in {root}:{END} {notebooks}")

# Sphinx labels
project = 'ImmunoGit'
copyright = '2025, SDG'
author = 'SDG'
release = '0.2-dev'

# Sphinx
extensions = [
    'nbsphinx',
    'myst_nb',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# nbsphinx 
nbsphinx_execute = 'force' # 'force' better than 'always'
nbsphinx_timeout = 60
nbsphinx_kernel_name = 'python3'
nbsphinx_allow_errors = True
