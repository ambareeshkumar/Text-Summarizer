from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.ModelEvaluation import ModelEvaluation
from TextSummarizer.logging import logging




class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        logging.info("Model Evaluation Pipeline Started")
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()
        logging.info("Model Evaluation Pipeline Completed")