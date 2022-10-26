#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]
    r = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name),
        params={
            "per_page": 10,
        }
        )
    for i in r.json():
        print("{}: {}\
        ".format(i.get("sha"), i.get("commit").get("author").get("name")))
