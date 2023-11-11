#!/usr/bin/python3
""" fetch https://alx-intranet.hbtn.io/status"""


import urllib.request as req

if __name__ == "__main__":
    with req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        msg = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(msg)))
        print("\t- content: {}".format(msg))
        print("\t- utf8 content: {}".format(msg.decode("utf-8")))
