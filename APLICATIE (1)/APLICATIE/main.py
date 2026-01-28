"""
Punct de intrare pentru aplicația Hangman 3D
"""

import sys
import os

# Adaugă src la path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.hangman_3d import create_app, setup_logging, get_logger

# Setup logging
setup_logging(log_dir="logs")
logger = get_logger(__name__)

if __name__ == '__main__':
    logger.info("Starting Hangman 3D application")
    
    # Pornește Flask app
    logger.info("Starting Flask development server")
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
