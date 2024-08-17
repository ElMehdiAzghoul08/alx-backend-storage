#!/usr/bin/env python3
"""Module"""


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic function"""
    return list(mongo_collection.find({"topics": topic}))
