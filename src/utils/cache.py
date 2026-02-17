"""
Caching utility module.
Provides simple in-memory caching with TTL support.
"""
import time
from typing import Any, Optional
from src.config import Config
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class Cache:
    """Simple in-memory cache with TTL support."""
    
    def __init__(self, ttl: int = None):
        """
        Initialize cache.
        
        Args:
            ttl: Time-to-live in seconds. If None, uses Config.CACHE_TTL
        """
        self._cache = {}
        self._ttl = ttl or Config.CACHE_TTL
        self._enabled = Config.CACHE_ENABLED
    
    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve value from cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value if exists and not expired, None otherwise
        """
        if not self._enabled:
            return None
            
        if key in self._cache:
            value, timestamp = self._cache[key]
            if time.time() - timestamp < self._ttl:
                logger.debug(f"Cache hit for key: {key}")
                return value
            else:
                logger.debug(f"Cache expired for key: {key}")
                del self._cache[key]
        
        logger.debug(f"Cache miss for key: {key}")
        return None
    
    def set(self, key: str, value: Any) -> None:
        """
        Store value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
        """
        if not self._enabled:
            return
            
        self._cache[key] = (value, time.time())
        logger.debug(f"Cached value for key: {key}")
    
    def clear(self) -> None:
        """Clear all cache entries."""
        self._cache.clear()
        logger.info("Cache cleared")
    
    def delete(self, key: str) -> None:
        """
        Delete specific cache entry.
        
        Args:
            key: Cache key to delete
        """
        if key in self._cache:
            del self._cache[key]
            logger.debug(f"Deleted cache entry for key: {key}")
