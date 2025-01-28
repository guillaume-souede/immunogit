"""
MODULES
"""
import asyncio
from playwright.async_api import async_playwright
import nest_asyncio
from bs4 import BeautifulSoup
import re
import os
import json
import subprocess
import sys
from pprint import pprint
import zipfile as z
import requests
import git
from pathlib import Path

try:
    from bioservices import BioModels
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bioservices"])
    from bioservices import BioModels

""" 
CONSTANTS 
"""
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

""" 
PATHS 
"""
repo = git.Repo('.', search_parent_directories=True)
root_path = repo.working_tree_dir
print(root_path)
bm_sbml_path = Path(root_path) / "models" / "BioModels" / "SBML"

os.makedirs(os.path.join(root_path, "models/BioModels/SBML"), exist_ok=True)
os.makedirs(os.path.join(root_path, "models/Reactome/SBML"), exist_ok=True)
os.makedirs(os.path.join(root_path, "models/Reactome/SBGN"), exist_ok=True)
os.makedirs(os.path.join(root_path, "metadata"), exist_ok=True)
print("Structure Ok.")

md_path = Path(repo.working_tree_dir) / "metadata"
all_md_path = md_path / "metadata_all.json"
bio_md_path = md_path / "metadata_BioModels.json"
rea_md_path = md_path / "metadata_Reactome.json"