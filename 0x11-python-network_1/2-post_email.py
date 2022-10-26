#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {
        email: email,
    }
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page)
