import pandas as pd
from diamond_price_predication import logger
from sklearn.linear_model import ElasticNet
import joblib
from diamond_price_predication.entity.config_entity import DataTrainingConfig
import os

class DataTrainer: 
    def __init__(self, config=DataTrainingConfig): 
        self.config=config
        
    def training(self): 
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        x_train=train_data.drop([self.config.target_column], axis=1)
        logger.info(f"x_train data : {x_train.head()}\n\n")
        
        x_test=test_data.drop([self.config.target_column], axis=1)
        logger.info(f"x_test data {x_test.head()}\n\n")
        
        y_train=train_data[[self.config.target_column]]
        logger.info(f"y_train data {y_train.head()}\n\n")
        
        y_test=test_data[[self.config.target_column]]
        logger.info(f"y_test data : {y_test.head()}\n\n")
        
        lr=ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        lr.fit(x_train, y_train)
        
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        
        
        
        
    