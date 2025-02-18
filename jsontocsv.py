import json
import datetime
import pandas as pd
import os

# Function to convert timestamp
def convert_timestamp(timestamp):
    if isinstance(timestamp, str) and timestamp.startswith("/Date(") and timestamp.endswith(")/"):
        timestamp = int(timestamp[6:-2]) / 1000
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return timestamp

addresses = []

#+ folder loop
folder_path = './data'
# List all files in the folder
files = os.listdir(folder_path)

for file_name in files:
    file_path = os.path.join(folder_path, file_name)

    # Load JSON data with the correct encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract address data
    for item in data:
        address = {
            'ListingId': item.get('ListingId'),
            'Address': item.get('Address'),
            'District': item.get('District'),
            'Suburb': item.get('Suburb'),
            'Region': item.get('Region'),
            'Area': item.get('Area', '0'),
            'LandArea': item.get('LandArea', '0'),
            'Bathrooms': item.get('Bathrooms'),
            'Bedrooms': item.get('Bedrooms'),
            'Parking': item.get('Parking'),
            'TotalParking': item.get('TotalParking', '0'),
            'StartDate': convert_timestamp(item.get('StartDate', 'N/A')),
            'EndDate': convert_timestamp(item.get('EndDate', 'N/A')),
            'RateableValue': item.get('RateableValue', '0'),
        }
        addresses.append(address)

#- folder loop

# Save data to CSV file
df = pd.DataFrame(addresses)
df.to_csv('addresses.csv', index=False)
