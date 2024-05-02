import os
from box import BoxError
import yaml
from box import ConfigBox
from pathlib import Path
from typing import Any
# from ensure import ensure_annotations

from TextSummarizer.logging import logging

# @ensure_annotations
def read_yaml(file_path):
    """
    Read yaml file and return a ConfigBox object.
    :param file_path:
    :return a ConfigBox object:
    """
    logging.info("Initiating read_yaml function")
    try:
        with open(file_path, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file:{file_path} loaded Successfully")
            return ConfigBox(content)
    except BoxError:
        raise ValueError("Could not read yaml file: {}".format(file_path))
    except FileNotFoundError:
        logging.info(f"Could not find yaml file: {file_path}")
        raise ValueError("Could not find yaml file: {}".format(file_path))

# @ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    Create directories
    :param path_to_directories:
    :param verbose:
    :return:
    """
    try:
        logging.info("Initiating create_directories function")

        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"Created directory {path}")
    except Exception as e:
        logging.info(f"Could not create directory {path}")
        raise ValueError("Could not create directory: {}".format(path))

# @ensure_annotations
def get_size(path:Path) -> str:
    """
    :param path:
    :return size of file in kb:

    """
    logging.info("Initiating get_size function")

    try:
        size_in_kb = round(os.path.getsize(path))
        logging.info(f"Size of file {path} is {size_in_kb} KB")
        return f"{size_in_kb} KB"
    except FileNotFoundError:
        logging.info(f"Could not find file {path}")
        raise ValueError("Could not find  file: {}".format(path))