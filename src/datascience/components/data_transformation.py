import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
from src.datascience.config.configuration import DataTransformationConfig
import pandas as pd



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

        ## we gonna perform train test split
    def train_test_split(self):
        """Splitting the data into train and test sets"""
        logger.info("Splitting the data into train and test sets")

        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data split completed")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)