from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import pandas as pd
import numpy as np
import joblib
from diamond_price_predication import logger
from diamond_price_predication.entity.config_entity import ModelEvaluationConfig
from diamond_price_predication.utils.common import save_json
from pathlib import Path




class ModelEvaluation: 
    def __init__(self, config= ModelEvaluationConfig): 
        self.config=config
        
        
    def Evaluation(self, actual, predicted):
        
        mse=mean_squared_error(actual , predicted)
        rms=np.sqrt(mean_squared_error(actual, predicted))
        r2score=r2_score(actual, predicted)
        
        return mse, rms, r2score 
    
    def save_result(self): 
        
        model= joblib.load(self.config.model_)  
        logger.info(f"model loaded sucessfully: {model}")
        
        test_data=pd.read_csv(self.config.test_data_path)
        logger.info(f"Test data sucessfullt {test_data.head()}")
        
        x_test=test_data.drop([self.config.target_column], axis=1)
        y_test=test_data[[self.config.target_column]]
        
        y_predict_=model.predict(x_test)
        
        (mse, rms, r2score)=self.Evaluation(y_test, y_predict_)
        
        # logger.info(f"Mean squared error: {mse}, root_mean_error: {rms}, root_mean: {r2score}")
        
        
        score={"MSE": mse, "RMS": rms, "r2score": r2score}
        
        save_json(path=Path(self.config.metric_file), data=score)
        
        logger.info(f"Metric score saved {score}")
        
                
        