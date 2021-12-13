#!/usr/bin/env python3
"""
Contains function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    Args:
        mongo_collection: Mongo db collection name

    Returns:
        Documents found in collection
    """
    return mongo_collection.find()
