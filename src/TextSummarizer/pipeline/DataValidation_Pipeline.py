from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.DataValidation import DataValidation
from TextSummarizer.logging import logging



class DataValidationPipeline:

    def __init__(self):
        pass

    def main(self):
        logging.info("Data Validation Pipeline Started")
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exist()
        logging.info("Data Validation Pipeline Completed")
