#!/usr/bin/env python3
"""Module"""


from pymongo import MongoClient


def log_stats():
    """log_stats function"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_counts = {
        method: collection.count_documents({"method": method})
        for method in methods}
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {methods_counts[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
