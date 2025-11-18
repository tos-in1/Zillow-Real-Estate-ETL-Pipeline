# =======================================================================
#                             DATA INGESTION
# ======================================================================

# ingesting data from local storage into the system 
import pandas as pd
import json

file_path = "C:/Oluwatosin_Git/Real_Estate_Data_Pipeline/data/raw_data/2025-11-18.json"

with open(file_path) as f:
    data = json.load(f)
df = pd.json_normalize(data["data"])
homes = df
print(homes[:5])

# ------------------------ TABLE PREPARATION ---------------------------
rows = []
column_names = ["zpid", "home_address", "state", "city", "zipcode", "latitude",
                "longitude", "bedrooms", "bathrooms", "living_area", "lot_size", 
                "year_built", "property_type", "price", "price_sqft", "status",
                "days_on_zillow"]

# ---------------------------- TABLE FIILING ----------------------------
# Looping through the data'
for index, home in homes.iterrows():
    zpid =              home["zpid"]
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

    tuple_of_records = (zpid, home_address, state, city, zipcode, latitude,
                longitude, bedrooms, bathrooms, living_area, lot_size, 
                year_built, property_type, price, price_sqft, status,
                days_on_zillow)
    
    rows.append(tuple_of_records)
print(rows)