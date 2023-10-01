import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "diseaseClassification"

list_of_files = [
    ".github/workflows/.gitkeep" #idea is to create a file in order to commit an empty project
    , f"src/{project_name}/__init__.py"
    , f"src/{project_name}/components/__init__.py"
    , f"src/{project_name}/utils/__init__.py"
    , f"src/{project_name}/config/configuration.py"
    , f"src/{project_name}/pipeline/__init__.py"
    , f"src/{project_name}/entity/__init__.py"
    , f"src/{project_name}/constants/__init__.py"
    , "config/config.yaml"
    , "dvc.yaml"
    , "params.yaml"
    ,"requirements.txt"    
    , "setup.py"
    , "pre-tests/trials.ipynb"
    , "templates/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath) # use Path to handle slashes on paths for os
    filedir, filename  = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the {filename}.")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists.")

