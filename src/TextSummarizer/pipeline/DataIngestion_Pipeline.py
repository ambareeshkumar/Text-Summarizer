from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.DataIngestion import DataIngestion
from TextSummarizer.logging import logging



class DataIngestion_Pipeline:

    def __init__(self):
        pass

    def main(self):
        logging.info("Data Ingestion Pipeline Started")
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()
        logging.info("Data Ingestion Pipeline Completed")