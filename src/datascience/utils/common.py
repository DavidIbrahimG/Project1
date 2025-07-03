import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError



@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (str): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading YAML file {path_to_yaml}: {e}")
        raise ValueError(f"Error reading YAML file {path_to_yaml}: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while reading YAML file {path_to_yaml}: {e}")
        raise ValueError(f"An unexpected error occurred while reading YAML file {path_to_yaml}: {e}")
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created or already exists.")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to save in the JSON file.
    """
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
            logger.info(f"Data saved to JSON file {path}.")
    except Exception as e:
        logger.error(f"Error saving data to JSON file {path}: {e}")
        raise ValueError(f"Error saving data to JSON file {path}: {e}")
    

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file and returns it as a ConfigBox object.
    
    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        ConfigBox: Content of the JSON file as a ConfigBox object.
    """
    with open(path) as f:
        content = json.load(f)
        logger.info(f"JSON file {path} loaded successfully.")
        return ConfigBox(content)


@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Saves data to a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        data (Any): Data to save in the binary file.
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Data saved to binary file {path}.")
    except Exception as e:
        logger.error(f"Error saving data to binary file {path}: {e}")
        raise ValueError(f"Error saving data to binary file {path}: {e}")
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Data loaded from the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Data loaded from binary file {path}.")
        return data
    except Exception as e:
        logger.error(f"Error loading data from binary file {path}: {e}")
        raise ValueError(f"Error loading data from binary file {path}: {e}")