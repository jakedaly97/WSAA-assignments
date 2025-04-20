# assignment03-cso.py
# Author: Jake Daly

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en" # URL of the CSO API

def getAll(): # Sends a GET request to the CSO API and returns the response as a JSON object
    response = requests.get(url)
    return response.json()

if __name__ == "__main__": 
    with open ("cso.json", "wt") as fp: # Open file for writing text
        print(json.dumps(getAll()), file=fp) # Converts JSON to string and writes it to the file

# Resources
# URL of the CSO API for the dataset FIQ02, https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en
# making a request, https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
