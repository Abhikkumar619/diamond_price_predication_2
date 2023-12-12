import os
from pathlib import Path
import logging

project_name='diamond_price_predication'

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s] : %(message)s:')

list_of_file=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirement.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
]

for filepath in list_of_file:
    file_path=Path(filepath)
    # logging.info(filepath)
    
    file_dir, file_name=os.path.split(file_path)
    
    logging.info(f"file_directories : {file_dir} file name :{file_name}")
    
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"directories created: {file_dir} for file {file_name}")
        
    if (not os.path.exists(file_path) or (os.path.getsize(filepath))):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"created empty file {file_path}")
    else: 
        logging.info(f"{file_name} already exist")
        
        
    
    
