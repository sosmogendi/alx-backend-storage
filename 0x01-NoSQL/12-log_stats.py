#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    print(f'{total_logs} logs')

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('HTTP Methods:')
    for method in http_methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check_count} status check')
