import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="EV Demand Intelligence AU",
    page_icon="⚡",
    layout="wide"
)

# =========================
# Header Section
# =========================
st.title("⚡ EV Demand Forecasting Dashboard")
st.markdown("### Real-Time EV Charging Demand Intelligence Across Australia")
st.markdown("---")

# =========================
# Sidebar
# =========================
st.sidebar.header("🔧 Prediction Controls")

day = st.sidebar.slider(
    "Select Day of Year",
    min_value=1,
    max_value=365,
    value=180
)

# =========================
# KPI Summary Section
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Stations", "500")
col2.metric("Total Chargers", "951")
col3.metric("Baseline MAE", "6.55")
col4.metric("Model Type", "Linear Regression")

st.markdown("---")

# =========================
# Prediction Section
# =========================
st.subheader("📊 Predicted National Demand")

try:
    response = requests.get(
        f"http://127.0.0.1:8000/predict?day_of_year={day}"
    )
    prediction = response.json()["predicted_demand"]

    st.metric(
        label=f"Predicted Demand for Day {day}",
        value=f"{prediction:.2f} units"
    )

except:
    st.error("API not running. Start FastAPI server.")
    prediction = None

st.markdown("---")

# =========================
# Trend Visualization
# =========================
st.subheader("📈 Annual Demand Trend Simulation")

days = np.arange(1, 366)

try:
    predictions = []
    for d in days:
        r = requests.get(
            f"http://127.0.0.1:8000/predict?day_of_year={d}"
        )
        predictions.append(r.json()["predicted_demand"])

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(days, predictions, linewidth=2)
    ax.set_xlabel("Day of Year")
    ax.set_ylabel("Predicted Demand")
    ax.set_title("Predicted EV Charging Demand Trend (National)")
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)

except:
    st.warning("Cannot load trend chart. API may not be running.")

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown(
    "Built with **FastAPI + Streamlit + Machine Learning** | "
    "EV Demand & Energy Intelligence Project"
)


import plotly.express as px
import pandas as pd

st.subheader("🗺️ EV Charging Station Map")

# Load cleaned dataset
df_map = pd.read_csv("etl/ev_stations_clean.csv")

# Remove invalid coordinates
df_map = df_map.dropna(subset=["latitude", "longitude"])

fig = px.scatter_mapbox(
    df_map,
    lat="latitude",
    lon="longitude",
    color="state",
    size="charger_count",
    hover_name="station_name",
    hover_data=["charger_count"],
    zoom=4,
    height=600
)

fig.update_layout(mapbox_style="carto-darkmatter")

st.plotly_chart(fig, width="stretch")