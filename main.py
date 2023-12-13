from diamond_price_predication import logger
from diamond_price_predication.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from diamond_price_predication.pipeline.stage_2_data_validation import DataValidationPipeline
from diamond_price_predication.pipeline.stage_03_data_transformation import DataTransformationPipeline

"""
stage_name= "Data_Ingestion_stage"

try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>.stage  {stage_name} Started>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e: 
        raise e
    
"""  
stage_name="Data_validation_stage"    
try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>... STAGE {stage_name} STARTED >>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>> STAGE {stage_name} ENDED >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e: 
    raise e

stage_name= "DataTransformation Stage"

try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} STARTED >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
except Exception as e: 
    raise e
    