#!/usr/bin/env python3
"""Module"""


def insert_school(mongo_collection, **kwargs):
    """insert_school function"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
