#!/usr/bin/env python3
"""
Contains a function that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    Args:
        mongo_collection: pymongo collection object
        kwargs: dictionary of objects to insert
    Returns:
        id of the new document
    """
    doc_id = mongo_collection.insert(kwargs)
    return doc_id
