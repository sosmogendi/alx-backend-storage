#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

def list_all(mongo_collection):
    """ List all documents in Python """
    all_documents = mongo_collection.find()

    if mongo_collection.count_documents({}) == 0:
        return []

    return list(all_documents)

