# TESTING CODES

import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()


# Creation of environment variables to protect sensitive data
url = os.getenv("url")
API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")

# Calling API
querystring = {"location":"houston, tx",
               "output":"json",
               "status":"forSale",
               "sortSelection":"newest",
               "listing_type":"by_owner_other",
               "doz":"30"""}

headers = {
	"x-rapidapi-key": API_KEY,
	"x-rapidapi-host": API_HOST
    }

# make request
response = requests.get(url, headers=headers, params=querystring)

# error handling using try and except
try:
    data = response.json()
except ValueError:
    print("Error: non JSON received")
    print(response.text)
    exit(1)

# Creating a storage folder in local machine
today = datetime.now().strftime("%Y-%m-%d")
folder_path = os.path.join