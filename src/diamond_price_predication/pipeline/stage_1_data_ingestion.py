from diamond_price_predication.config.configuration import ConfigurationManger
from diamond_price_predication.components.data_ingestation import DataIngeston
from diamond_price_predication import logger


stage_name= "Data_Ingestion_stage"

class DataIngestionTrainingPipeline: 
    def __init__(self) -> None:
        pass
    
    def main(self):

        try: 
            obj_config_manager=ConfigurationManger()
            data_ingestion_config=obj_config_manager.get_data_ingestion_config()
            dataingestion=DataIngeston(data_ingestion_config)
            dataingestion.download_file()
            # dataingestion.extract_zip_file()
            
        except  Exception as e: 
            raise e
        
if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>.stage  {stage_name} Started>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e