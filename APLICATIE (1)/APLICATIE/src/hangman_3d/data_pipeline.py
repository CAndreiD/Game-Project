"""
Pipeline pentru colectare, procesare și export de date
"""

import logging
from .api_client import APIClient
from .data_processor import DataProcessor
from .csv_exporter import CSVExporter
from .visualizer import DataVisualizer

logger = logging.getLogger(__name__)


class DataPipeline:
    """
    Pipeline complet pentru colectare și prelucrare de date
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Inițializează pipeline-ul
        
        Args:
            output_dir: Directorul de output
        """
        self.api_client = APIClient()
        self.processor = DataProcessor()
        self.csv_exporter = CSVExporter(output_dir)
        self.visualizer = DataVisualizer(output_dir)
    
    def run_full_pipeline(self) -> dict:
        """
        Rulează pipeline-ul complet
        
        Returns:
            Dicționar cu rezultatele
        """
        logger.info("Starting full data pipeline")
        
        results = {
            "posts_csv": None,
            "posts_chart": None,
            "users_csv": None,
            "users_chart": None
        }
        
        try:
            # 1. Colectează postări
            logger.info("Step 1: Collecting posts from API")
            posts = self.api_client.fetch_posts(limit=10)
            
            if posts:
                # Exportă în CSV
                results["posts_csv"] = self.csv_exporter.export_data(posts, "posts_data")
                
                # Creează grafic
                user_counts = self.processor.count_by_field(posts, 'userId')
                results["posts_chart"] = self.visualizer.create_bar_chart(
                    user_counts, 
                    "Posts by User", 
                    "posts_by_user"
                )
            
            # 2. Colectează utilizatori
            logger.info("Step 2: Collecting users from API")
            users = self.api_client.fetch_users(limit=5)
            
            if users:
                # Exportă în CSV
                results["users_csv"] = self.csv_exporter.export_data(users, "users_data")
                
                # Creează grafic cu conturile pe città
                city_counts = self.processor.count_by_field(users, 'address')
                if city_counts:
                    results["users_chart"] = self.visualizer.create_pie_chart(
                        {f"User {i}": 1 for i in range(len(users))},
                        "Users Distribution",
                        "users_distribution"
                    )
            
            logger.info("Pipeline completed successfully")
            
        except Exception as e:
            logger.error(f"Error in pipeline: {e}")
        
        return results
