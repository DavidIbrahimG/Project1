import os
import urllib.request as request
from src.datascience import logger
from zipfile import ZipFile
from src.datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.datascience.entity.config_entity import DataIngestionConfig



## Data ingestion component

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    ## Downloading the zip file from the source URL
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename} with headers: \n{headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists. Skipping download.")



    ## Unzipping the downloaded file
    def extract_zip_file(self):
        """
        zip_file_path: str
        extract the file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file to {unzip_path}")

