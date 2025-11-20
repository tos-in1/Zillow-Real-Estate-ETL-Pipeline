"""
LOAD CLEANED DATA INTO POSTGRESQL (Zillow Pipeline)

This script connects to a PostgreSQL database using credentials stored in environment 
variables and loads a cleaned Zillow CSV file into the `zillow_properties` table.

Steps performed:
- Load DB credentials from .env
- Connect to PostgreSQL via psycopg2
- Verify connection by listing public tables
- Read the cleaned CSV file
- Bulk-insert data using `cursor.copy_from()`
- Commit the transaction

Output: cleaned Zillow data successfully loaded into PostgreSQL.
"""

# importing the required libraries
import psycopg2
import os
from dotenv import load_dotenv
import csv
load_dotenv()

# Bringing forward the database credentials through environment variable
POSTGRESQL_HOST         = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_PORT         = os.getenv("POSTGRESQL_PORT")
POSTGRESQL_USERNAME     = os.getenv("POSTGRESQL_USERNAME")
POSTGRESQL_PASSWORD     = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_DATABASE     = os.getenv("POSTGRESQL_DATABASE")

# Connecting to PostgreSQL
connection = psycopg2.connect(
    host = POSTGRESQL_HOST,
    database = POSTGRESQL_DATABASE,
    user = POSTGRESQL_USERNAME,
    password = POSTGRESQL_PASSWORD,
    port = POSTGRESQL_PORT
)

cursor = connection.cursor()
print("SUCCESS! Connected to PosgreSQL")

# testing out the connection to view table created
cursor.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema='public';
""")
print(cursor.fetchall())

csv_path = "C:/Oluwatosin_Git/Real_Estate_Data_Pipeline/data/cleaned_data/2025-11-19.csv"


# loading into the database from local storage
with open(csv_path, "r") as file:
    next(file)
    cursor.copy_from(file, "zillow_properties", sep=',', null="")

connection.commit()
print("SUCCESS: Loaded into DB")
