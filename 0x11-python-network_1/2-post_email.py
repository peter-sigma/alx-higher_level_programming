#!/usr/bin/python3
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen

""" take URL and email and send POST request to passed URL with email as parameter"""

if __name__ == "__main__":
    url = argv[1]
    mail = {"email": argv[2]}
    msg = parse.urlencode(mail).encode("ascii")
    req = Request(url, msg)

    with urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
