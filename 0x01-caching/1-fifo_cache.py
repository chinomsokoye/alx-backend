#!/usr/bin/python3
""" Create class FIFOCache, inherits from BaseCaching, a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class FIFOCache """

    def __init__(self):
        """ Initializes class/function"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """ function put """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """ function get """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
