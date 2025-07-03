from src.datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.datascience.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from pathlib import Path
from src.datascience.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, 
                 params_file_path=PARAMS_FILE_PATH, 
                 schema_file_path=SCHEMA_FILE_PATH):
        

        self.config = read_yaml(str(config_file_path))
        self.params = read_yaml(str(params_file_path))
        self.schema = read_yaml(str(schema_file_path))

        ## Create directories if they do not exist
        create_directories([self.config.artifacts_root])

    ## Data Ingestion Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
        
    
    ## Data Validation Configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        # Ensure the root directory exists
        create_directories([Path(config.root_dir)])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=Path(config.STATUS_FILE),
            unzip_data_dir=Path(config.unzip_data_dir),
            all_schema=schema
        )

        return data_validation_config
    

    ## Data Transformation Configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """Returns Data Transformation Configuration"""
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path)
        )
        return data_transformation_config
