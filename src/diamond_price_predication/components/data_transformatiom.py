from diamond_price_predication.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from diamond_price_predication import logger
import os
import pandas as pd



class DataTransformation: 
    def __init__(self, config=DataTransformationConfig) -> None:
        self.config=config
       
        
    def TrainingTesting_split(self):
        data=pd.read_csv(self.config.data_dir)
        logger.info(f"Dataset of diamond predication: {data.head()}\n\n")
        
        train, test=train_test_split(data)
        logger.info(f"Training data {train.head()}\n\n")
        logger.info(f"Testing data {test.head()}\n\n")
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f" Training and testing data sucessfully {train.shape, test.shape}")