#!/usr/bin/python3
""" Create class MRUCache, inherits from BaseCaching, a caching system """

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ class MRUCache """

    def __init__(self):
        """ Initializes class/function """
        super().__init__()
        self.mru_order = OrderedDict()

    def put(self, key, item):
        """ function put """
        if not key or not item:
            return
        self.cache_data[key] = item
        self.mru_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.mru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.mru_order) > BaseCaching.MAX_ITEMS:
            self.mru_order.popitem(last=False)

        self.mru_order.move_to_end(key, False)

    def get(self, key):
        """ function get """
        if key in self.cache_data:
            self.mru_order.move_to_end(key, False)
            return self.cache_data[key]
        return None
