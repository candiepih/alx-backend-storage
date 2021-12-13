#!/usr/bin/env python3
"""
Contains function that provides some stats about
Nginx logs stored in MongoDB:
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Prints some stats about Nginx logs stored in MongoDB

    Args:
        mongo_collection: MongoDB collection object
    Returns:
        Nothing
    """
    num_logs = mongo_collection.count_documents({})
    print("{} logs".format(num_logs))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        docs = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, docs))
    route = mongo_collection.count_documents({"method": "GET",
                                              "path": "/status"})
    print("{} status check".format(route))


if __name__ == "__main__":
    with MongoClient() as client:
        db = client.logs
        collection = db.nginx
        log_stats(collection)
