"""
Factory pentru crearea aplicației Flask
"""

from typing import Optional
from flask import Flask
from .config import config, FLASK_ENV
from .routes import game_bp
import logging

logger = logging.getLogger(__name__)


def create_app(config_name: Optional[str] = None) -> Flask:
    """
    Crează și configurează aplicația Flask
    
    Args:
        config_name: Nume config ('development', 'testing', 'production')
        
    Returns:
        Instanță Flask configurată
    """
    app = Flask(__name__, 
                template_folder='../../templates',
                static_folder='../../static')
    
    # Determină config
    if config_name is None:
        config_name = FLASK_ENV
    
    config_class = config.get(config_name, config['default'])
    app.config.from_object(config_class)
    
    # Înregistrează blueprint-uri
    app.register_blueprint(game_bp)
    
    # Data API Routes
    @app.route('/api/data/pipeline', methods=['GET'])
    def run_data_pipeline():
        """Rulează pipeline-ul de colectare și prelucrare de date"""
        try:
            from .data_pipeline import DataPipeline
            pipeline = DataPipeline(output_dir="output")
            results = pipeline.run_full_pipeline()
            return {"status": "success", "results": results}, 200
        except Exception as e:
            logger.error(f"Error running pipeline: {e}")
            return {"status": "error", "message": str(e)}, 500
    
    @app.route('/api/data/status', methods=['GET'])
    def data_status():
        """Returnează status-ul colectării de date"""
        return {"status": "ready", "version": "1.0.0"}, 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Nu a fost găsit"}, 404
    
    @app.errorhandler(500)
    def server_error(error):
        return {"error": "Eroare server"}, 500
    
    return app
