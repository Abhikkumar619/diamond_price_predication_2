from diamond_price_predication.config.configuration import ConfigurationManger
from diamond_price_predication.components.data_validation import DataValidation
from diamond_price_predication import logger


stage_name="Data_validation_stage"

class DataValidationPipeline: 
    def __init__(self)-> None: 
        pass
    def main(self):
        try: 
            obj=ConfigurationManger()
            validationConfig=obj.get_validation_config()
            datavalidation=DataValidation(validationConfig)
            datavalidation.validate_all_columns()
        except Exception as e: 
            raise e
    
    
if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>... STAGE {stage_name} STARTED >>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>> STAGE {stage_name} ENDED >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e
    
