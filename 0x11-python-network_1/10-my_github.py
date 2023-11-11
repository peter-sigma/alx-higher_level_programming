#!/usr/bin/python3
import sys
import requests
from requests.auth import HTTPBasicAuth

"""take github credentials and use GitHub API to display a GitHub ID
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
