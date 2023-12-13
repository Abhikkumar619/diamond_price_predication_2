from diamond_price_predication.config.configuration import ConfigurationManger
from diamond_price_predication.components.data_transformatiom import DataTransformation
from diamond_price_predication import logger

stage_name= "DataTransformation Stage"

class DataTransformationPipeline: 
    def __init__(self): 
        pass
    
    def main(self): 
        try: 
            obj=ConfigurationManger()
            transformation_config=obj.get_data_transformation_config()
            datatranf=DataTransformation(transformation_config)
            datatranf.TrainingTesting_split()
        except Exception as e: 
            raise e
                
                
                
if __name__ == "__main__": 
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} STARTED >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
    except Exception as e: 
        raise e
        
        





