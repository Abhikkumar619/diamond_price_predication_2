from diamond_price_predication.constant import *
from diamond_price_predication.utils.common import read_yaml, create_dicectories,save_json
from diamond_price_predication.entity.config_entity import DataIngestionConfig
from diamond_price_predication.entity.config_entity import DataValidationConfig
from diamond_price_predication.entity.config_entity import DataTransformationConfig
from diamond_price_predication.entity.config_entity import DataTrainingConfig
from diamond_price_predication.entity.config_entity import ModelEvaluationConfig


class ConfigurationManger:
    def __init__(self, config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH
                 ): 
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)
        self.schema=read_yaml(schema_file_path)
        
        create_dicectories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self)-> DataIngestionConfig: 
        config=self.config.data_ingestion
        create_dicectories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir)
        
        return data_ingestion_config
    
    def get_validation_config(self)-> DataValidationConfig: 
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        
        create_dicectories([config.root_dir])
        
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_dir=config.unzip_data_dir, 
            status_file=config.STATUS_FILE,
            all_schema=schema
        )
        return data_validation_config
    
    
    def get_data_transformation_config(self)-> DataTransformationConfig: 
        
        
        config=self.config.data_transformation
        create_dicectories([config.root_dir])
        
        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_dir=config.data_dir
        )
        
        return data_transformation_config
    
    
            
    def get_data_training_Config(self)-> DataTrainingConfig: 
        
        config=self.config.data_trainer
        schema=self.schema.TARGET_COLUMN
        params=self.params.ElasticNet
        
        create_dicectories([config.root_dir])
        
        
        datatraing_Config=DataTrainingConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            l1_ratio=params.alpha,
            alpha=params.l1_ratio,
            target_column=schema.name
            )
        return datatraing_Config
    
    def get_model_evaluation_config(self)-> ModelEvaluationConfig: 
            
        config=self.config.model_evaluation
        schema=self.schema.TARGET_COLUMN
        params=self.params.ElasticNet
            
        create_dicectories([config.root_dir])
            
            
        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir, 
            test_data_path=config.test_data_path, 
            model_=config.model_path,
            metric_file=config.metric_file_path,
            all_parmas=params, 
            target_column=schema.name)
        return model_evaluation_config
            
            
            
            
            
        
        
        
    