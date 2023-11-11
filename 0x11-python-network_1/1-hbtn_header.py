#!/usr/bin/python3
""" Send request to URL and display value of X-Request-Id"""
from sys import argv
import urllib.request as req


if __name__ == "__main__":
    url = argv[1]
    with req.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
