import os
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import yaml
from diamond_price_predication import logger
import json
import joblib
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox: 
    try: 
        with open(path_to_yaml) as yaml_file: 
            content=yaml.safe_load(yaml_file)
            logger.info(f"Yaml file read {path_to_yaml}")
            
            return ConfigBox(content)
    except Exception as e: 
        raise e
        
@ensure_annotations
def create_dicectories(path_to_dict: list):
    for path in path_to_dict: 
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directories file is creted {path}")
 

@ensure_annotations        
def save_json(path:Path, data: dict): 
    with open(path, 'w') as f: 
        json.dump(data, f)
        
    logger.info(f"Json file saved at {path}")
    
@ensure_annotations
def load_json(path_json: Path)-> ConfigBox: 
    with open(Path) as f: 
        content=json.load(f)
    logger.info(f"Json file loaded sucessfully {content}")
    return ConfigBox(content)

@ ensure_annotations
def save_bin(data:any, path:Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path=Path)->Any:
    data=joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path)->str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"_{size_in_kb} KB"
    

    
        

        

