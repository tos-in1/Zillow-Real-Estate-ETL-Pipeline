
/*
==================================================================================================================
DDL Script: Create zillow_properties Table
==================================================================================================================
	Script Purpose: The purpose of this script is to create a table "zillow_properties", dropping existing 
	tables if they already exist.

	To re-define the DDL structure of 'zillow_properties' Tables, RUN this script
==================================================================================================================
*/

IF OBJECT_ID ('zillow_properties', 'U') IS NOT NULL
	DROP TABLE bronze.crm_cust_info;

CREATE TABLE zillow_properties(
property_id			VARCHAR(20) 	NOT NULL PRIMARY KEY,
home_address		VARCHAR(100) 	NOT NULL,
state				VARCHAR(10) 	NOT NULL,
city				VARCHAR(10) 	NOT NULL,
zipcode				VARCHAR(10) 	NOT NULL,
latitude			FLOAT			NOT NULL,
longitude			FLOAT			NOT NULL,
bedroom				INT				NOT NULL,
bathroom			FLOAT			NOT NULL,
living_area			INT,
lot_size			FLOAT,
year_built			INT,
property_type		VARCHAR(20)		NOT NULL,
price				INT				NOT NULL,
price_sqft			INT				NOT NULL,
status				VARCHAR(10)		NOT NULL,
days_on_zillow		INT				NOT NULL
);
