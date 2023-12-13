from diamond_price_predication.components.model_evaluation import ModelEvaluation
from diamond_price_predication import logger
from diamond_price_predication.config.configuration import ConfigurationManger


stage_name="Model_Evaluation"

class ModelEvaluationPipeline:
    def __init__(self): 
        pass
    
    def main(self): 
        try: 
             
            configmanager=ConfigurationManger()
            model_evaluation_config=configmanager.get_model_evaluation_config() 
            modelevaluation=ModelEvaluation(model_evaluation_config)
            # modelevaluation.Evaluation()
            modelevaluation.save_result()

        except Exception as e: 
            raise e
        
if __name__ == "__main__": 
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} Stared >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e:
        raise e   
        
        