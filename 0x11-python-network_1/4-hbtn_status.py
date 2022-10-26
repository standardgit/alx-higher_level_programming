#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    r = request.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t\
".format(type(r.text), r.text))
