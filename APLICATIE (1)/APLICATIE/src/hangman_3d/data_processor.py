"""
Procesor de date - prelucrarea datelor colectate din API
"""

from typing import Dict, List, Any
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class DataProcessor:
    """
    Procesor pentru prelucrarea și transformarea datelor colectate
    """
    
    @staticmethod
    def filter_by_field(data: List[Dict[str, Any]], field: str, value: Any) -> List[Dict[str, Any]]:
        """
        Filtrează datele după o anumită valoare de câmp
        
        Args:
            data: Lista de dicționare
            field: Câmpul după care se filtrează
            value: Valoarea căutată
            
        Returns:
            Lista filtrată
        """
        filtered = [item for item in data if item.get(field) == value]
        logger.info(f"Filtered {len(data)} items by {field}={value}, result: {len(filtered)}")
        return filtered
    
    @staticmethod
    def extract_fields(data: List[Dict[str, Any]], fields: List[str]) -> List[Dict[str, Any]]:
        """
        Extrage doar anumite câmpuri din date
        
        Args:
            data: Lista de dicționare
            fields: Lista câmpurilor de extras
            
        Returns:
            Lista cu doar câmpurile selectate
        """
        extracted = []
        for item in data:
            extracted_item = {field: item.get(field) for field in fields if field in item}
            extracted.append(extracted_item)
        
        logger.info(f"Extracted {len(fields)} fields from {len(data)} items")
        return extracted
    
    @staticmethod
    def aggregate_by_field(data: List[Dict[str, Any]], group_field: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Grupează datele după un anumit câmp
        
        Args:
            data: Lista de dicționare
            group_field: Câmpul după care se grupează
            
        Returns:
            Dicționar cu datele grupate
        """
        aggregated = {}
        for item in data:
            key = str(item.get(group_field, 'unknown'))
            if key not in aggregated:
                aggregated[key] = []
            aggregated[key].append(item)
        
        logger.info(f"Aggregated {len(data)} items into {len(aggregated)} groups by {group_field}")
        return aggregated
    
    @staticmethod
    def count_by_field(data: List[Dict[str, Any]], field: str) -> Dict[str, int]:
        """
        Numără ocurențele pentru fiecare valoare a unui câmp
        
        Args:
            data: Lista de dicționare
            field: Câmpul de numărare
            
        Returns:
            Dicționar cu contoare
        """
        counts = {}
        for item in data:
            key = str(item.get(field, 'unknown'))
            counts[key] = counts.get(key, 0) + 1
        
        logger.info(f"Counted {len(data)} items by field {field}")
        return counts
    
    @staticmethod
    def get_statistics(data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculează statistici generale despre date
        
        Args:
            data: Lista de dicționare
            
        Returns:
            Dicționar cu statistici
        """
        stats = {
            "total_items": len(data),
            "timestamp": datetime.now().isoformat(),
            "fields": list(data[0].keys()) if data else [],
            "processed": True
        }
        
        logger.info(f"Generated statistics for {len(data)} items")
        return stats
