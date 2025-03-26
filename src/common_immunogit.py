"""
MODULES
"""
import asyncio
import json
import logging
import os
import re
import subprocess
import sys
import zipfile as z
from collections import defaultdict
from pathlib import Path

import git
import matplotlib.pyplot as plt
import pandas as pd
from bioservices import BioModels
from bs4 import BeautifulSoup
from matplotlib_venn import venn3
from playwright.async_api import async_playwright
import requests
import nest_asyncio

""" 
CONSTANTS 
"""
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

""" 
SETUP LOGGER 
"""
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

""" 
PATHS 
"""
try:
    repo = git.Repo('.', search_parent_directories=True)
    root_path = Path(repo.working_tree_dir)
except git.exc.InvalidGitRepositoryError:
    logger.error("Not inside a valid Git repository. Exiting.")
    sys.exit(1)

logger.info(f"Root path: {root_path}")

bm_sbml_path = root_path / "models" / "BioModels" / "SBML"
reactome_sbml_path = root_path / "models" / "Reactome" / "SBML"
reactome_sbgn_path = root_path / "models" / "Reactome" / "SBGN"
metadata_path = root_path / "metadata"

# Create directories
for path in [bm_sbml_path, reactome_sbml_path, reactome_sbgn_path, metadata_path]:
    path.mkdir(parents=True, exist_ok=True)

logger.info("Directory structure set up successfully.")

""" 
METADATA FILES 
"""
all_md_path = metadata_path / "metadata_all.json"
bio_md_path = metadata_path / "metadata_BioModels.json"
rea_md_path = metadata_path / "metadata_Reactome.json"