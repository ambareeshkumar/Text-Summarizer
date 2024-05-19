from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.ModelTrainer import ModelTrainer
from TextSummarizer.logging import logging


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()