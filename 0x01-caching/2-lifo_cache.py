#!/usr/bin/python3
""" Create class LIFOCache, inherits from BaseCaching, a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ class LIFOCache """

    def __init__(self):
        """ Initializes class/function """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """ function put """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """ function get """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
