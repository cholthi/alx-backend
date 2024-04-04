#!/usr/bin/env python3
"""Basic Cache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic Caching class"""
    def put(self, key, item):
        """ Put an item at a key in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get cache item at a key"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
