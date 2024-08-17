#!/usr/bin/env python3
"""Module"""


from pymongo import MongoClient


def top_students(mongo_collection):
    """top_students function"""
    pipeline = [
        {
            '$project': {
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
