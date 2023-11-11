#!/usr/bin/python3
import requests
from sys import argv


"""
Sends a request to URL and display value of X-Request-Id in the response header

Usage: ./5-hbtn_header.py <URL>
"""

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)

    print(req.headers.get("X-Request-Id"))
