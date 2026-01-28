"""
Configurare logging pentru aplicație
"""

import logging
import os
from datetime import datetime


def setup_logging(log_dir: str = "logs", log_level=logging.INFO) -> None:
    """
    Configurează logging pentru întreaga aplicație
    
    Args:
        log_dir: Directorul pentru log files
        log_level: Nivelul de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Creează directorul de logs dacă nu există
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Formatul pentru logs
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    
    # Handler pentru fișier
    log_filename = os.path.join(log_dir, f"app_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(log_level)
    file_formatter = logging.Formatter(log_format, datefmt=date_format)
    file_handler.setFormatter(file_formatter)
    
    # Handler pentru console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_formatter = logging.Formatter(log_format, datefmt=date_format)
    console_handler.setFormatter(console_formatter)
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Log inițial
    root_logger.info(f"Logging initialized - Level: {logging.getLevelName(log_level)}")
    root_logger.info(f"Log file: {log_filename}")


def get_logger(name: str) -> logging.Logger:
    """
    Obține un logger pentru un modul
    
    Args:
        name: Numele modulului (__name__)
        
    Returns:
        Logger instance
    """
    return logging.getLogger(name)
