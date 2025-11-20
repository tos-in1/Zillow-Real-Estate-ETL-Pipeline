"""
TRANSFORMING ZILLOW RAW DATA

Script description: This script loads the raw Zillow JSON response, flattens it into a DataFrame,
and prepares it for cleaning and analysis. It extracts key fields such as
location details, pricing, property characteristics, and listing metadata.

Steps performed:
- Flatten raw JSON using pandas.json_normalize
- Select and organize relevant Zillow fields
- Build a structured table of property records
- Convert the data into a clean, tabular DataFrame
- Save the transformed dataset as a CSV file in local storage

Output: A structured, clean-ready CSV file containing normalized Zillow property data.
"""


# importing the appropraite library
import pandas as pd
import json
import os
from datetime import datetime

# Flattening json file for proper viewing
file_path = "C:/Oluwatosin_Git/Real_Estate_Data_Pipeline/data/raw_data/2025-11-18.json"

with open(file_path) as f:
    data = json.load(f)
df = pd.json_normalize(data["data"])
homes = df

# Flattening json file for proper viewing
file_path = "C:/Oluwatosin_Git/Real_Estate_Data_Pipeline/data/raw_data/2025-11-18.json"

with open(file_path) as f:
    data = json.load(f)
df = pd.json_normalize(data["data"])
homes = df


# ------------------------ TABLE PREPARATION ---------------------------
rows = []
column_names = ["property_id", "home_address", "state", "city", "zipcode", "latitude",
                "longitude", "bedrooms", "bathrooms", "living_area", "lot_size", 
                "year_built", "property_type", "price", "price_sqft", "status",
                "days_on_zillow"]


# ---------------------------- TABLE FIILING ----------------------------
# Looping through the data'
for index, home in homes.iterrows():
    property_id =       home["zpid"]
    home_address =      home["address.streetAddress"]
    state =             home["address.state"]
    city =              home["address.city"]
    zipcode =           home["address.zipcode"]
    latitude =          home["location.latitude"]
    longitude =         home["location.longitude"]
    bathrooms =         home["bathrooms"]
    bedrooms =          home["bedrooms"]
    living_area =       home["livingArea"]
    lot_size =          home["lotSizeWithUnit.lotSize"]
    year_built =        home["yearBuilt"]
    property_type =     home["propertyType"]
    price =             home["price.value"]
    price_sqft =        home["price.pricePerSquareFoot"]
    status =            home["listing.marketingStatus"]
    days_on_zillow =    home["daysOnZillow"]

    tuple_of_records = (property_id, home_address, state, city, zipcode, latitude,
                longitude, bedrooms, bathrooms, living_area, lot_size, 
                year_built, property_type, price, price_sqft, status,
                days_on_zillow)
    
    rows.append(tuple_of_records)

# Printing into dataframe
print(rows)

# inserting column names
df = pd.DataFrame(rows, columns=column_names)

# Proper indexing - indexing starting from 0
df.index = df.index + 1

# ---------------------------------------------- DATA CLEANING PROPER ------------------------------------------------

# To have a smoother and faster work, creating a class that houses
# all cleaning functions

class Zillow_data_cleaner:
    def __init__(self, df):
         self.df = df.copy()
        
    # Function 1: Converting datatypes
    def fix_dtypes(self):
        if 'bathroom' in self.df.columns:
            self.df['bathroom'] = self.df['bathroom'].astype(float)
        if 'bedroom' in self.df.columns:
            self.df['bedroom'] = self.df['bedroom'].astype(int)
        if 'living_area' in self.df.columns:
            self.df['living_area'] = self.df['living_area'].astype(int)
        if 'lot_size' in self.df.columns:
            self.df['lot_size'] = self.df['lot_size'].astype(float)
        if 'price' in self.df.columns:
            self.df['price'] = self.df['price'].astype(int)
        return self
    
    # Function 2: Handling of missing values
    def missing(self):
        # Drop rows where these fields are missing
        self.df = self.df.dropna(subset=['property_id', 'home_address'])
        return self
    
    # Function 3: Remove Duplicates
    def remove_duplicates(self):
        # Drop rows where these fields are missing
        self.df = self.df.drop_duplicates(subset='property_id', keep='first')
        return self
    
    # Function 4: standardize
    def standadize(self):
        self.df["property_type"] = self.df["property_type"].str.replace("singleFamily", "Single Family")
        self.df["status"] = self.df["status"].str.replace("active", "Active")
        self.df["state"] = self.df["state"].str.replace("TX", "Texas")
        return self
    
    # Function 5: Roundingoff
    def rounding_off(self):
        self.df["lot_size"] = self.df["lot_size"].round(1)
        return self
    
    def clean_all(self):
        # Run all the cleaning at a go
        return self.fix_dtypes().missing().remove_duplicates().standadize().rounding_off().df
    
# Apply cleaner and realigning index
cleaner = Zillow_data_cleaner(df)
clean_df = cleaner.clean_all().reset_index(drop=True)
clean_df.index = clean_df.index + 1

# Storing the cleaned property data on local storage
# Get the directory where this particular script is located
BASE_DIR = os.getcwd()

today_date = datetime.now().strftime("%Y-%m-%d")  # Getting today's date
folder_path = os.path.join(BASE_DIR, "data", "cleaned_data") # File path creation
os.makedirs(folder_path, exist_ok=True)

# Creating the file path 
file_path = f"{folder_path}/{today_date}.csv"

# Dumping into the filepath the API response
clean_df.to_csv(file_path, index=False)

print(f"Saved to: {file_path}")