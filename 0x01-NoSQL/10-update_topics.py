#!/usr/bin/env python3
"""Module"""


def update_topics(mongo_collection, name, topics):
    """update_topics function"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
