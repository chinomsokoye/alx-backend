#!/usr/bin/env python3
"""
Simple helper function named index_range
takes two arguments page and page_size
Returns a tuple of size two (start index, end index)
corresponding to the range of indexes to return in a list
for those particular pagination parameters
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Prototype: def index_range(page:int, page_size: int)
    Returns a Tuple of size
    """
    index = page * page_size - page_size
    index_ = index + page_size
    return (index, index_)
