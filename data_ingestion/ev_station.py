import requests
import pandas as pd
import time

API_KEY = "6a2abdfb-31cf-4686-9202-6e708b5858c3"

URL = "https://api.openchargemap.io/v3/poi/"

PARAMS = {
    "output": "json",
    "countrycode": "AU",
    "maxresults": 500,
    "compact": True,
    "verbose": False
}

HEADERS = {
    "X-API-Key": API_KEY,
    "User-Agent": "EV-Demand-Intelligence-Project",
    "Accept": "application/json"
}

print("Fetching EV charging station data for Australia...")

response = requests.get(URL, params=PARAMS, headers=HEADERS) # Make GET request to the API with specified parameters and headers

if response.status_code != 200:  # Check if the request was successful (status code 200 means OK)
    raise Exception(f"API request failed with status code {response.status_code}")

data = response.json()  # convert response to JSON format and making it a Python list of dictionaries
print(f"Retrieved {len(data)} EV stations")

df = pd.json_normalize(data) # Convert list of dicts to a flat table (DataFrame) for easier manipulation and analysis

timestamp = time.strftime("%Y%m%d_%H%M%S")
output_path = f"data_ingestion/ev_stations_raw_{timestamp}.csv"

df.to_csv(output_path, index=False)

print(f"Raw EV data saved to {output_path}")
