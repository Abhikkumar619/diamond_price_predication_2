import joblib
import numpy as np
from pathlib import Path
import pandas as pd
from diamond_price_predication import logger


class PredictionPipeline: 
    def __init__(self)-> None: 
        self.model=joblib.load(Path('artifacts\data_trainer\model.joblib'))
        logger.info(f"Model loaded sucessfully in PredictionPipeline { self.model}")
        
    def predict(self, data): 
        prediction=self.model.predict(data)
        
        return prediction