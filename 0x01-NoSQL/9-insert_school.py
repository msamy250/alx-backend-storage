#!/usr/bin/env python3
"""DB implementation"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
