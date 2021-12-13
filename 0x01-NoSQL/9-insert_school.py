#!/usr/bin/env python3
"""
Contains a function that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    Args:
        mongo_collection: pymongo collecetion object
        kwargs: dictionary of objects to insert
    Returns:
        Id of the new document
    """
    id = mongo_collection.insert(kwargs)
    return id
