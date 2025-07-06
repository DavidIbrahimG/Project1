from src.datascience import logger
from src.datascience.pipelines.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipelines.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipelines.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipelines.model_trainer_pipeline import ModelTrainingTrainingPipeline
from src.datascience.pipelines.model_evaluation_pipeline import ModelEvaluationTrainingPipeline


stage_name = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()    
    logger.info(f">>>> stage {stage_name} completed successfully <<<<")
except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Data Validation Stage"
try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>> stage {stage_name} completed successfully <<<<")
except Exception as e:
    logger.exception(e)
    raise e


stage_name = "Data Transformation Stage"
try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    data_transformation = DataTransformationTrainingPipeline()  
    data_transformation.initiate_data_transformation()
    logger.info(f">>>> stage {stage_name} completed successfully <<<<")
except Exception as e:
    logger.exception(e)
    raise e
    

stage_name = "Model Training Stage"
try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    # Code to initiate model training pipeline
    model_trainer = ModelTrainingTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>> stage {stage_name} completed successfully <<<<")
except Exception as e:
    logger.exception(e)
    raise e



stage_name = "Model Evaluation Stage"
try:
    logger.info(f">>>> stage {stage_name} started <<<<")
    # Code to initiate model evaluation pipeline
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>> stage {stage_name} completed successfully <<<<")
except Exception as e:
    logger.exception(e)
    raise e