import requests
import sys

try:
    n = input("How much bitcoin do you want to buy? ")
    try:
        float(n)
    except:
        sys.exit
except requests.RequestException:
    ...