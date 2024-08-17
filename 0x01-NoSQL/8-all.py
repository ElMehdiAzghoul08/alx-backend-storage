#!/usr/bin/env python3
"""Module"""


def list_all(mongo_collection):
    """list_all function"""
    return list(mongo_collection.find())
