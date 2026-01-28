"""
Exportor de date în format CSV
"""

import csv
from typing import Dict, List, Any
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class CSVExporter:
    """
    Exportă datele în fișiere CSV
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Inițializează exportorul CSV
        
        Args:
            output_dir: Directorul de export
        """
        self.output_dir = output_dir
        self._ensure_output_dir()
    
    def _ensure_output_dir(self):
        """Se asigură că directorul de output există"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logger.info(f"Created output directory: {self.output_dir}")
    
    def export_data(self, data: List[Dict[str, Any]], filename: str) -> str:
        """
        Exportă datele în CSV
        
        Args:
            data: Lista de dicționare
            filename: Numele fișierului (fără extensie)
            
        Returns:
            Calea către fișier
        """
        if not data:
            logger.warning(f"No data to export for {filename}")
            return ""
        
        filepath = os.path.join(self.output_dir, f"{filename}.csv")
        
        try:
            fieldnames = list(data[0].keys())
            
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            
            logger.info(f"Successfully exported {len(data)} rows to {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Error exporting CSV: {e}")
            return ""
    
    def export_aggregated(self, aggregated_data: Dict[str, Any], filename: str) -> str:
        """
        Exportă datele agregate în CSV
        
        Args:
            aggregated_data: Dicționar cu datele agregate
            filename: Numele fișierului (fără extensie)
            
        Returns:
            Calea către fișier
        """
        if not aggregated_data:
            logger.warning(f"No aggregated data to export for {filename}")
            return ""
        
        filepath = os.path.join(self.output_dir, f"{filename}.csv")
        
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['key', 'value'])
                
                for key, value in aggregated_data.items():
                    if isinstance(value, (int, float)):
                        writer.writerow([key, value])
                    else:
                        writer.writerow([key, str(value)])
            
            logger.info(f"Successfully exported aggregated data to {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Error exporting aggregated CSV: {e}")
            return ""
    
    def get_export_path(self, filename: str) -> str:
        """Obține calea completă pentru un fișier de export"""
        return os.path.join(self.output_dir, f"{filename}.csv")
