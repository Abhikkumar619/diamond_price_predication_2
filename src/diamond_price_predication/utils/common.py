"""
The functionality which we using everywhere in the project, such reading the yaml file, 
the function which is used to read the yaml file  we write here.
"""

import os
from box import ConfigBox
from pathlib import Path
from box.exceptions import BoxValueError
import yaml
from src.diamond_price_predication import logger
from ensure import ensure_annotations
import json
import joblib



@ensure_annotations
def read_yaml_file(file_path: Path)->ConfigBox:
    """
    Read yaml file and return 
    """
    try: 
        with open(file_path) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {file_path} is loaded")
            return ConfigBox(content)
        
    except BoxValueError: 
        raise ValueError("Yaml file is empty")
    except Exception as e: 
 
 
 
        raise e
@ensure_annotations  
def create_directories(path_to_directories:list, verbose=True):
    """
    Created list of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        
        if verbose: 
            logger.info(f"Created directories as {path}")
 
 
 
            
@ensure_annotations           
def save_json(path:Path, data:dict):
    """
    Save json data
    path: path to json file.
    data: data to be saved in json file.
    """
    with open(path, 'w') as f:
        json.dump(data, f)
    logger.info(f"Json file is saved at path {path}")
 
 
  
@ensure_annotations  
def load_json(path: Path)->ConfigBox:
    with open(path) as f:
        content=json.load(f)
    logger.info(f"Json file is loaded sucessfully from : {path}")
    return ConfigBox(content)
 
    
@ensure_annotations
def save_bin(data:any, path:Path):
    joblib.dump(value=data, file_path=Path)
    logger.info(f"Binary file loaded from: {path}")
    return data


            