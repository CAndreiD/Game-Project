"""
Hangman 3D - Joc interactiv cu rendering 3D
"""

from .app import create_app
from .logger import setup_logging, get_logger

__version__ = "1.0.0"
__all__ = ["create_app", "setup_logging", "get_logger"]
