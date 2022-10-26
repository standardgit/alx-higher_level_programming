#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.error
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.URLError as e:
       print(f"Error code: {e.code}")
