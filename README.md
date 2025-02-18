# JSON Data Extractor

This Python script reads JSON files from a specified folder, extracts address data, and saves the data to a CSV file.

## Prerequisites

Make sure you have the following Python packages installed:

- pandas

You can install these packages using pip:

```bash
pip install pandas
```

## Usage

1. Place your JSON files in a folder named data in the same directory as this script.

1. Run the script:
```bash
python script_name.py
```

Replace script_name.py with the name of your Python script.

## Script Details

The script performs the following tasks:

1. Imports necessary libraries.

1. Defines a function convert_timestamp to convert timestamp strings to a readable date format.

1. Iterates through all JSON files in the data folder.

1. Loads JSON data from each file.

1. Extracts address-related information from each JSON object.

1. Saves the extracted data to a CSV file named addresses.csv.

## Example JSON Structure

The script expects JSON files with the following structure:
```json
[
    {
        "ListingId": "12345",
        "Address": "123 Main St",
        "District": "Central",
        "Suburb": "Suburbia",
        "Region": "Region",
        "Area": "150",
        "LandArea": "500",
        "Bathrooms": "2",
        "Bedrooms": "3",
        "Parking": "Garage",
        "TotalParking": "2",
        "StartDate": "/Date(1609459200000)/",
        "EndDate": "/Date(1612137600000)/",
        "RateableValue": "500000"
    }
]
```

Output
The script will generate a CSV file named addresses.csv with the extracted address data.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


Feel free to modify the README file based on your specific needs. If you need any more help, just let me know! 😊

Have you got any other Python projects you're working on?
