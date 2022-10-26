#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
