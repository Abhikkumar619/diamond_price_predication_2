from diamond_price_predication.entity.config_entity import DataValidationConfig
from diamond_price_predication import logger
import pandas as pd


class DataValidation: 
    def __init__(self, config: DataValidationConfig): 
        self.config=config
        
        
        
    def validate_all_columns(self)->bool: 
        try: 
            validation_status: None
            data=pd.read_csv(self.config.unzip_dir)
            all_cols=list(data.columns)
            logger.info(f" Columns: {all_cols}")
            
            all_schema=self.config.all_schema.keys()
            
            logger.info(f"All schema {all_schema}")
            
            for col in all_cols: 
                if col not in all_schema: 
                    
                    
                    validation_status=False
                    
                    with open(self.config.status_file, 'w') as f: 
                        f.write(f"Validation status: {validation_status}")
                    
            else: 
                validation_status=True
                with open(self.config.status_file,'w') as f: 
                    f.write(f" Validation status: {validation_status}")
                    
            return validation_status
            
            
        
        except Exception as e: 
            raise e