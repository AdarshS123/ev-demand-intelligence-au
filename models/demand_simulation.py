import pandas as pd
import numpy as np

df = pd.read_csv("models/ev_stations_standardized.csv")

# Create date range
dates = pd.date_range(start="2025-01-01", end="2025-12-31") # Simulate for one year

simulation_data = [] # List to hold simulated records

for _, row in df.iterrows(): 
    for date in dates:
        base_demand = row["charger_count"] * np.random.uniform(5, 10)   # Base demand proportional to charger count with some randomness

        # Weekend effect
        if date.weekday() >= 5:
            base_demand *= 1.2

        simulation_data.append({  
            "date": date,
            "state": row["state"],
            "station_id": row["station_id"],
            "daily_demand": round(base_demand, 2)
        })      

sim_df = pd.DataFrame(simulation_data)

sim_df.to_csv("models/simulated_demand.csv", index=False)

print("Simulated demand dataset created.")