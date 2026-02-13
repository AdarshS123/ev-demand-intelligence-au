from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(title="EV Demand Forecast API")

# Load trained model
model = joblib.load("api/model.pkl")

@app.get("/")
def home():
    return {"message": "EV Demand Forecast API is running."}

@app.get("/predict")
def predict(day_of_year: int):
    """
    Predict EV demand for a given day of year (1-365)
    """
    prediction = model.predict(np.array([[day_of_year]]))
    return {
        "day_of_year": day_of_year,
        "predicted_demand": round(float(prediction[0]), 2)
    }