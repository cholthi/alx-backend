#!/usr/bin/env python3
"""Provides a function index_range"""


def index_range(page: int, page_size) -> tuple:
    """Returns pagination params into a list of data"""
    offset = page * page_size
    limit = (page - 1) * page_size
    return (offset, limit)
