#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

def update_topics(mongo_collection, school_name, new_topics):
    """ Changes all topics of a school document based on the name """
    query = {"name": school_name}
    new_values = {"$set": {"topics": new_topics}}

    mongo_collection.update_many(query, new_values)
