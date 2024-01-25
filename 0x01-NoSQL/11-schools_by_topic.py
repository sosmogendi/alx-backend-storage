#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

def schools_by_topic(mongo_collection, search_topic):
    """ Returns the list of schools having a specific topic """
    query = {"topics": search_topic}
    matching_schools = mongo_collection.find(query)
    return list(matching_schools)
