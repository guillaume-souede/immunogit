"""
MODULES
"""
import asyncio
from playwright.async_api import async_playwright
import nest_asyncio
import os
import subprocess
import sys
import zipfile as z
import requests
import json
from re import *
from bs4 import BeautifulSoup
"""
PATHS
"""
current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))

os.makedirs(os.path.join(root_path, "models/BioModels/SBML"), exist_ok=True)
os.makedirs(os.path.join(root_path, "models/Reactome/SBML"), exist_ok=True)
os.makedirs(os.path.join(root_path, "models/Reactome/SBGN"), exist_ok=True)
os.makedirs(os.path.join(root_path, "metadata"), exist_ok=True)
print("Structure : Done.")

"""
COMMON VARIABLES
"""
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'