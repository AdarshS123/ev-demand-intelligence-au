import pandas as pd
from sqlalchemy import create_engine

# Update credentials if needed
DB_USER = "postgres"
DB_PASSWORD = "Adarsh123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ev_intelligence"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Load clean CSV
df = pd.read_csv("C:/Users/adars/OneDrive/Desktop/project/ev-demand-intelligence-au/etl/ev_stations_clean.csv")  
# Insert into PostgreSQL
df.to_sql(
    "ev_stations",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded into PostgreSQL successfully")
print(f"Total rows inserted: {len(df)}")