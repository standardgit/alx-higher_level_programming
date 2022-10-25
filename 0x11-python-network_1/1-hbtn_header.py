#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        header_request_id = response.headers.get("X-Request-Id")
        print(header_request_id)
