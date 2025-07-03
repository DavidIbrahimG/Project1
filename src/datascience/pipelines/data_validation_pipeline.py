from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation


stage_name = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        logger.info(f"{stage_name} completed successfully.")

if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {stage_name} started <<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>> stage {stage_name} completed successfully <<<<")
    except Exception as e:
        logger.exception(e)
        raise e