from diamond_price_predication.config.configuration import ConfigurationManger
from diamond_price_predication.components.data_training import DataTrainer
from diamond_price_predication import logger

stage_name="Model_Training"

class DataTrainingPipeline:
    def __init__(self): 
        pass
    
    def main(self): 

        try: 
            obj=ConfigurationManger()
            trainingConfig=obj.get_data_training_Config()
            modeltraining= DataTrainer(trainingConfig)
            modeltraining.training()
        except Exception as e: 
            raise e
if __name__ == "__main__": 
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} STARTED >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        obj=DataTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Ended>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except  Exception as e: 
        raise e