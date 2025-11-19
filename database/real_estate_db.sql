DROP TABLE IF EXISTS zillow_properties;
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
living_area			INT				NOT NULL,
lot_size			FLOAT			NOT NULL,
year_built			INT				NOT NULL,
property_type		VARCHAR(20)		NOT NULL,
price				INT				NOT NULL,
price_sqft			INT				NOT NULL,
status				VARCHAR(10)		NOT NULL,
days_on_zillow		INT				NOT NULL
);
