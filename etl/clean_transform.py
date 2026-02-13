import pandas as pd
import glob
import ast

# -----------------------------
# 1) Load Latest Raw File
# -----------------------------
raw_files = glob.glob("data_ingestion/ev_stations_raw_*.csv")

if not raw_files:
    raise FileNotFoundError("No raw EV station files found.")

latest_file = max(raw_files)

print(f"Loading raw data: {latest_file}")
df = pd.read_csv(latest_file)

# -----------------------------
# 2) Basic Column Selection
# -----------------------------
clean_df = pd.DataFrame({
    "station_id": df["ID"],
    "station_name": df["AddressInfo.Title"],
    "state": df["AddressInfo.StateOrProvince"],
    "latitude": df["AddressInfo.Latitude"],
    "longitude": df["AddressInfo.Longitude"],
    "operator_id": df["OperatorID"],
    "last_verified": df["DateLastVerified"],
})

# -----------------------------
# 3) Safe Charger Count
# -----------------------------
def count_chargers(conn):
    try:
        parsed = ast.literal_eval(conn)
        if isinstance(parsed, list):
            return len(parsed)
        return 0
    except:
        return 0

clean_df["charger_count"] = df["Connections"].apply(count_chargers)

# -----------------------------
# 4) Drop Rows with Missing Geo
# -----------------------------
clean_df = clean_df.dropna(subset=["latitude", "longitude"])

# -----------------------------
# 5) Standardise State Names
# -----------------------------
clean_df["state"] = clean_df["state"].astype(str).str.upper().str.strip()

state_mapping = {
    "VICTORIA": "VIC",
    "VIC": "VIC",
    "NEW SOUTH WALES": "NSW",
    "NSW": "NSW",
    "QUEENSLAND": "QLD",
    "QLD": "QLD",
    "WESTERN AUSTRALIA": "WA",
    "WA": "WA",
    "SOUTH AUSTRALIA": "SA",
    "SA": "SA",
    "TASMANIA": "TAS",
    "TAS": "TAS",
    "NORTHERN TERRITORY": "NT",
    "NT": "NT",
    "ACT": "ACT"
}

clean_df["state"] = clean_df["state"].map(state_mapping).fillna(clean_df["state"])

# Optional: Remove non-state entries (like councils)
valid_states = ["NSW", "VIC", "QLD", "WA", "SA", "TAS", "NT", "ACT"]
clean_df = clean_df[clean_df["state"].isin(valid_states)]

# -----------------------------
# 6) Save Clean Dataset
# -----------------------------
output_path = "etl/ev_stations_clean.csv"
clean_df.to_csv(output_path, index=False)

print(f"Cleaned data saved to {output_path}")
print(f"Total stations after cleaning: {len(clean_df)}")