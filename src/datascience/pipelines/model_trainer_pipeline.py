from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience import logger


STAGE_NAME = "Model Training Stage"

class ModelTrainingTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        # Load configuration
        configuration_manager = ConfigurationManager()
        config = configuration_manager.get_model_trainer_config()

        # Initialize model trainer
        model_trainer = ModelTrainer(config)

        # Train the model
        model_trainer.train()

        logger.info(f"{STAGE_NAME} completed successfully.")