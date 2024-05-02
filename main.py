from TextSummarizer.pipeline.DataIngestion_Pipeline import DataIngestion_Pipeline
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