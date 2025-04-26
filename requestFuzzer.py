#!/bin/python3

# importing the sys module so that we can
# use command line arguments for targetURL
import sys

# importing requests library to contact targetURL
import requests

def getResponse(targetURL):
# Banner
    print("""
    ================================
        Web App Brute Force Tool    
    ================================
    """)

# Take in Target URL from command line argv[1]
    res = requests.get(targetURL)

# Print target URL to terminal
    print("[*] Target URL:",targetURL)
    print("[*] response :\n", res.text)

if len(sys.argv) > 1:
    targetURL = sys.argv[1]
    getResponse(targetURL)

else:
    print("[*] i.e. 'http://example.com'")
    targetURL = input("Enter target URL: ")
    getResponse(targetURL)

# test
