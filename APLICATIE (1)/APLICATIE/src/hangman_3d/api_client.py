"""
Client pentru colectarea datelor din API-uri externe
"""

import requests
from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)


class APIClient:
    """
    Client pentru interacțiunea cu API-uri externe
    """
    
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        """
        Inițializează client-ul API
        
        Args:
            base_url: URL-ul bazei API
        """
        self.base_url = base_url
        self.timeout = 10
    
    def fetch_posts(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch-ează postări din API extern
        
        Args:
            limit: Numărul de postări de recuperat
            
        Returns:
            Listă cu datele postărilor
        """
        try:
            url = f"{self.base_url}/posts?_limit={limit}"
            logger.info(f"Fetching data from {url}")
            
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Successfully fetched {len(data)} posts")
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return []
    
    def fetch_users(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch-ează utilizatori din API extern
        
        Args:
            limit: Numărul de utilizatori de recuperat
            
        Returns:
            Listă cu datele utilizatorilor
        """
        try:
            url = f"{self.base_url}/users?_limit={limit}"
            logger.info(f"Fetching users from {url}")
            
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Successfully fetched {len(data)} users")
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching users: {e}")
            return []
    
    def fetch_comments(self, post_id: int = 1) -> List[Dict[str, Any]]:
        """
        Fetch-ează comentarii pentru o postare
        
        Args:
            post_id: ID-ul postării
            
        Returns:
            Listă cu comentariile
        """
        try:
            url = f"{self.base_url}/posts/{post_id}/comments"
            logger.info(f"Fetching comments from {url}")
            
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Successfully fetched {len(data)} comments")
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching comments: {e}")
            return []
