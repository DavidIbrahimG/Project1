from src.datascience import logger
from pathlib import Path
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation


stage_name = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as file:
                status = file.read().split(" ")[-1]
            if status == "True":
                logger.info(f">>>> stage {stage_name} started <<<<")
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
                logger.info(f">>>> stage {stage_name} completed successfully <<<<")
            else:
                logger.info(f">>>> stage {stage_name} skipped as data validation failed <<<<")
        except Exception as e:
            logger.exception(e)
            raise e


