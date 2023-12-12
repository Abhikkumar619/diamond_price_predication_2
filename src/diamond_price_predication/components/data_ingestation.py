from diamond_price_predication.entity.config_entity import DataIngestionConfig
import os
import urllib.request as request
from diamond_price_predication import logger
from diamond_price_predication.utils.common import get_size
import zipfile
from pathlib import Path



class DataIngeston: 
    def __init__(self, config: DataIngestionConfig): 
        self.config=config
        
    def download_file(self): 
        if not os.path.exists(self.config.local_data_file): 
            file_name, header=request.urlretrieve(url=self.config.source_url, filename=self.config.local_data_file)
            
            logger.info(f"{file_name} downloaded with header name {header}")
        else: 
            logger.info(f"File already exists size {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        try: 
            unzip_path=self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        except Exception as e:
            raise e