import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error

# Load simulated data
df = pd.read_csv("models/simulated_demand.csv")

# Aggregate to national daily demand
df = df.groupby("date")["daily_demand"].sum().reset_index()
df.columns = ["ds", "y"]

# Train Prophet
model = Prophet()
model.fit(df)

# Make forecast for same historical period
future = model.make_future_dataframe(periods=0)
forecast = model.predict(future)

# Extract actual and predicted values
actual = df["y"].values
predicted = forecast["yhat"].values

# Calculate MAE
mae_prophet = mean_absolute_error(actual, predicted)

print("Prophet MAE:", round(mae_prophet, 2))

# Save predictions for comparison
prophet_results = pd.DataFrame({
    "actual": actual,
    "prophet_pred": predicted
})

prophet_results.to_csv("models/prophet_predictions.csv", index=False)

print("Prophet predictions saved.")