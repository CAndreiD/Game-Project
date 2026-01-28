"""
Vizualizare date cu matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
from typing import Dict, List, Any
import os
import logging

logger = logging.getLogger(__name__)


class DataVisualizer:
    """
    Creează vizualizări grafice ale datelor
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Inițializează visualizatorul
        
        Args:
            output_dir: Directorul de salvare a imaginilor
        """
        self.output_dir = output_dir
        self._ensure_output_dir()
    
    def _ensure_output_dir(self):
        """Se asigură că directorul de output există"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logger.info(f"Created output directory: {self.output_dir}")
    
    def create_bar_chart(self, data: Dict[str, int], title: str, filename: str) -> str:
        """
        Creează un grafic cu bare
        
        Args:
            data: Dicționar cu date (cheie, valoare)
            title: Titlul graficului
            filename: Numele fișierului PNG (fără extensie)
            
        Returns:
            Calea către fișier
        """
        try:
            plt.figure(figsize=(10, 6))
            keys = list(data.keys())
            values = list(data.values())
            
            plt.bar(keys, values, color='steelblue', edgecolor='navy')
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel('Categorie', fontsize=12)
            plt.ylabel('Count', fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            
            filepath = os.path.join(self.output_dir, f"{filename}.png")
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            
            logger.info(f"Successfully created bar chart: {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Error creating bar chart: {e}")
            return ""
    
    def create_pie_chart(self, data: Dict[str, int], title: str, filename: str) -> str:
        """
        Creează un grafic pie
        
        Args:
            data: Dicționar cu date (cheie, valoare)
            title: Titlul graficului
            filename: Numele fișierului PNG (fără extensie)
            
        Returns:
            Calea către fișier
        """
        try:
            plt.figure(figsize=(10, 8))
            keys = list(data.keys())
            values = list(data.values())
            
            plt.pie(values, labels=keys, autopct='%1.1f%%', startangle=90)
            plt.title(title, fontsize=16, fontweight='bold')
            plt.tight_layout()
            
            filepath = os.path.join(self.output_dir, f"{filename}.png")
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            
            logger.info(f"Successfully created pie chart: {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Error creating pie chart: {e}")
            return ""
    
    def create_line_chart(self, data: Dict[str, List[int]], title: str, filename: str) -> str:
        """
        Creează un grafic liniar
        
        Args:
            data: Dicționar cu serii de date (nume_serie: [valori])
            title: Titlul graficului
            filename: Numele fișierului PNG (fără extensie)
            
        Returns:
            Calea către fișier
        """
        try:
            plt.figure(figsize=(12, 6))
            
            for label, values in data.items():
                plt.plot(range(len(values)), values, marker='o', label=label)
            
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel('Index', fontsize=12)
            plt.ylabel('Valoare', fontsize=12)
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
            filepath = os.path.join(self.output_dir, f"{filename}.png")
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            
            logger.info(f"Successfully created line chart: {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Error creating line chart: {e}")
            return ""
    
    def create_histogram(self, values: List[int], title: str, filename: str, bins: int = 20) -> str:
        """
        Creează un histogram
        
        Args:
            values: Lista de valori
            title: Titlul graficului
            filename: Numele fișierului PNG (fără extensie)
            bins: Numărul de intervale
            
        Returns:
            Calea către fișier
        """
        try:
            plt.figure(figsize=(10, 6))
            
            plt.hist(values, bins=bins, color='skyblue', edgecolor='black')
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel('Valoare', fontsize=12)
            plt.ylabel('Frecvență', fontsize=12)
            plt.tight_layout()
            
            filepath = os.path.join(self.output_dir, f"{filename}.png")
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            
            logger.info(f"Successfully created histogram: {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Error creating histogram: {e}")
            return ""
