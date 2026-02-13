import pandas as pd

df = pd.read_csv("etl/ev_stations_clean.csv")

# Standardize state names
state_mapping = {
    "VIC": "VICTORIA",
    "NSW": "NEW SOUTH WALES",
    "QLD": "QUEENSLAND",
    "WA": "WESTERN AUSTRALIA",
    "SA": "SOUTH AUSTRALIA",
    "TAS": "TASMANIA",
    "NT": "NORTHERN TERRITORY"
}

df["state"] = df["state"].replace(state_mapping)

# Remove clearly incorrect state entries
df = df[~df["state"].str.contains("DISTRICT|PASTORAL|AUTRALIA", na=False)]

df.to_csv("models/ev_stations_standardized.csv", index=False)

print("State names standardized.")
print(df["state"].value_counts())