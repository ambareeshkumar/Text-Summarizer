from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.DataTransformation import DataTransformation
from TextSummarizer.logging import logging



class DataTransformationPipeline:

    def __init__(self):
        pass

    def main(self):
        logging.info("Data Transformation Pipeline Started")
        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.convert()
        logging.info("Data Validation Pipeline Completed")
