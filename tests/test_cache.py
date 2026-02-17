import unittest
from src.utils.cache import Cache
import time

class TestCache(unittest.TestCase):

    def test_cache_set_and_get(self):
        """Test basic cache set and get operations."""
        cache = Cache(ttl=10)
        cache.set('test_key', 'test_value')
        value = cache.get('test_key')
        self.assertEqual(value, 'test_value')

    def test_cache_miss(self):
        """Test cache miss returns None."""
        cache = Cache()
        value = cache.get('nonexistent_key')
        self.assertIsNone(value)

    def test_cache_expiry(self):
        """Test cache entry expiration."""
        cache = Cache(ttl=1)  # 1 second TTL
        cache.set('test_key', 'test_value')
        
        # Should exist immediately
        value = cache.get('test_key')
        self.assertEqual(value, 'test_value')
        
        # Wait for expiry
        time.sleep(1.1)
        value = cache.get('test_key')
        self.assertIsNone(value)

    def test_cache_clear(self):
        """Test cache clear operation."""
        cache = Cache()
        cache.set('key1', 'value1')
        cache.set('key2', 'value2')
        cache.clear()
        self.assertIsNone(cache.get('key1'))
        self.assertIsNone(cache.get('key2'))

    def test_cache_delete(self):
        """Test cache delete specific entry."""
        cache = Cache()
        cache.set('key1', 'value1')
        cache.set('key2', 'value2')
        cache.delete('key1')
        self.assertIsNone(cache.get('key1'))
        self.assertEqual(cache.get('key2'), 'value2')
