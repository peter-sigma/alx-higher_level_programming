#!/usr/bin/python3
import requests
from sys import argv


""" POST an email
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    myrequest = requests.post(url, data=value)
    print(myrequest.text)
