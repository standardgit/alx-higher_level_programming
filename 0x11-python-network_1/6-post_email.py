#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}
    r = requests.post(url, data)
    print(r.text)
