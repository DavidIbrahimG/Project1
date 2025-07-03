from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion



stage_name = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
            pass
    
    def initiate_data_ingestion(self):
         config= ConfigurationManager()
         data_ingestion_config = config.get_data_ingestion_config()
         data_ingestion = DataIngestion(config=data_ingestion_config)
         data_ingestion.download_file()
         data_ingestion.extract_zip_file()
         logger.info(f"{stage_name} completed successfully.")


if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {stage_name} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>> stage {stage_name} completed successfully <<<<")
    except Exception as e:
        logger.exception(e)
        raise e