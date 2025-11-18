# TESTING CODES

import pandas as pd
from pandas import json_normalize
import json

file = "C:/Oluwatosin_Git/Real_Estate_Data_Pipeline/raw_data/2025-11-15.json"

with open(file, "r") as f:
    data = json.load(f)

print(data)


read = json_normalize(data)
print(read.head())
