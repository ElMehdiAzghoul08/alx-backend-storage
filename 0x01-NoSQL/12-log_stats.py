#!/usr/bin/env python3
"""Module"""


from pymongo import MongoClient


def log_stats():
    """log_stats function"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collect_of_logs = client.logs.nginx
    total = collect_of_logs.count_documents({})
    get = collect_of_logs.count_documents({"method": "GET"})
    post = collect_of_logs.count_documents({"method": "POST"})
    put = collect_of_logs.count_documents({"method": "PUT"})
    patch = collect_of_logs.count_documents({"method": "PATCH"})
    delete = collect_of_logs.count_documents({"method": "DELETE"})
    path = collect_of_logs.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
