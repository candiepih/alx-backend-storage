#!/usr/bin/env python3
"""
Contains a function that returns the list of school
having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Lists schools having specific topic
    Args:
        mongo_collection: pymongo collection object
        topic (string): string to search in topics

    Returns:
        List of schools with topic
    """
    return mongo_collection.find({"topics": topic})
