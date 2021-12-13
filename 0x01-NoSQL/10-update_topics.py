#!/usr/bin/env python3
"""
Contains a function that changes all topics
of a school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name (string): name of documents to search
        topics (list): list of strings of topics
    """
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
