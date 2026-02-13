import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("models/simulated_demand.csv")

# Convert date 
df["date"] = pd.to_datetime(df["date"])   # Ensure date is in datetime format for feature extraction
df["day_of_year"] = df["date"].dt.dayofyear  # Use day of year as a simple feature for baseline model

X = df[["day_of_year"]]
y = df["daily_demand"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Baseline MAE:", round(mae, 2))

results = pd.DataFrame({
    "actual": y_test.values,
    "baseline_pred": predictions
})

results.to_csv("models/baseline_predictions.csv", index=False)

import joblib

joblib.dump(model, "api/model.pkl")
print("Model saved successfully.")