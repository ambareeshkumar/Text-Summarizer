from TextSummarizer.pipeline.DataIngestion_Pipeline import DataIngestion_Pipeline
from TextSummarizer.pipeline.DataValidation_Pipeline import DataValidationPipeline
from TextSummarizer.pipeline.DataTransformationPipeline import DataTransformationPipeline
from TextSummarizer.pipeline.ModelTrainerPipeline import ModelTrainerPipeline

from TextSummarizer.logging import logging

STAGE_NAME = "Data Ingestion Pipeline"

try:
    logging.info(f"-------------- {STAGE_NAME} Started --------------")
    data_ingestion = DataIngestion_Pipeline()
    data_ingestion.main()
    logging.info(f"-------------- {STAGE_NAME} Completed --------------")
except Exception as e:
    logging.error(f"-------------- {STAGE_NAME} Failed --------------")
    raise e


STAGE_NAME = "Data Validation Pipeline"

try:
    logging.info(f"-------------- {STAGE_NAME} Started --------------")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f"-------------- {STAGE_NAME} Completed --------------")
except Exception as e:
    logging.error(f"-------------- {STAGE_NAME} Failed --------------")
    raise e


STAGE_NAME = "Data Transformation Pipeline"

try:
    logging.info(f"-------------- {STAGE_NAME} Started --------------")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logging.info(f"-------------- {STAGE_NAME} Completed --------------")
except Exception as e:
    logging.error(f"-------------- {STAGE_NAME} Failed --------------")
    raise e


STAGE_NAME = "Model Trainer Pipeline"

try:
    logging.info(f"-------------- {STAGE_NAME} Started --------------")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logging.info(f"-------------- {STAGE_NAME} Completed --------------")
except Exception as e:
    logging.error(f"-------------- {STAGE_NAME} Failed --------------")
    raise e

