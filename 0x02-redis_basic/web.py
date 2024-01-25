#!/usr/bin/env python3
""" Redis Module """

from functools import wraps
import redis
import requests
from typing import Callable

redis_conn = redis.Redis()

def count_requests(method: Callable) -> Callable:
    """ Decorator for counting requests """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Wrapper for decorator """
        redis_conn.incr(f"request_count:{url}")
        cached_html = redis_conn.get(f"cached_html:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html_content = method(url)
        redis_conn.setex(f"cached_html:{url}", 10, html_content)
        return html_content

    return wrapper

@count_requests
def get_page(url: str) -> str:
    """ Obtain the HTML content of a URL """
    response = requests.get(url)
    return response.text
