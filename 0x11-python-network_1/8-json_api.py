#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=data)
    try:
        first = response.json()
        if not first:
            print("No result")
        else:
            print("[{}] {}".format(first.get("id"), first.get("name")))
    except ValueError:
        print("Not a valid JSON")
