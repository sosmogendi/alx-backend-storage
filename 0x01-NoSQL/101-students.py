#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    top_students_result = mongo_collection.aggregate([
        {
            "$project": {
                "_id": 1,  # Explicitly include the _id field
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_students_result
