"""
REAL ESTATE DATA EXTRACTION AND STORAGE (Zillow API)

This script retrieves real estate listing data for Houston, Texas using the Zillow API (via RapidAPI). 
It serves as the data generation step in the pipeline by making an authenticated HTTP request and 
saving the raw API response for downstream processing.

The script performs the following tasks:

1. Loads environment variables (API credentials) for secure authentication.
2. Sends a GET request to the Zillow API with filters including:
   - location: Houston, TX
   - listing status: for sale
   - listing type: agent
   - sort order and price type
3. Extracts and prints the JSON response upon a successful API call.
4. Handles errors gracefully if a non-JSON response is returned.
5. Stores the raw API response locally in a timestamped JSON file inside:
      data/raw_data/YYYY-MM-DD.json

"""

#  importing the required variables
import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

# Get the directory where this particular script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Creation of environment variables to protect sensitive data
url = os.getenv("url")
API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")

# Calling API
url = url

querystring = {"location":"Houston, TX",
               "status":"forSale",
               "sort":"relevance",
               "sortType":"asc",
               "priceType":"listPrice",
               "listingType":"agent"}

headers = {
	"x-rapidapi-key": API_KEY,
	"x-rapidapi-host": API_HOST
}

# make request
response = requests.get(url, headers=headers, params=querystring)

# error handling using try and except
try:
    data = response.json()
    print("SUCCESS! - Data has been pulled from Zillow API")
except ValueError:
    print("Error: non JSON received")
    print(response.text)
    exit(1)


# ===================================================================
#                           DATA STORAGE
# ===================================================================
# Creating a storage folder in local machine
today_date = datetime.now().strftime("%Y-%m-%d")  # Getting today's date
folder_path = os.path.join(BASE_DIR, "data", "raw_data") # File path creation
os.makedirs(folder_path, exist_ok=True)

# Creating the file path 
file_path = f"{folder_path}/{today_date}.json"

# Dumping into the filepath the API response
with open(file_path, "w") as file:
    json.dump(response.json(), file, indent=4)