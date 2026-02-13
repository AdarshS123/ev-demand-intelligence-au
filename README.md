🚗⚡ EV Charging Demand & Infrastructure Intelligence – Australia
📌 Overview

Australia is rapidly transitioning toward electric vehicles (EVs), but infrastructure growth and charger distribution remain uneven across states.

This project builds an end-to-end EV Infrastructure Intelligence Platform that:

Ingests live EV charging station data

Cleans and standardizes inconsistent infrastructure records

Designs a PostgreSQL analytics schema

Computes infrastructure KPIs

Implements demand forecasting

Deploys predictions via a REST API

Visualizes insights through an interactive dashboard

The goal was not just to build a model — but to design a production-style analytics pipeline from raw data to deployed system.

🏗️ System Architecture
Open Charge Map API
        ↓
Data Ingestion (Python)
        ↓
ETL & Standardization
        ↓
PostgreSQL Database
        ↓
Analytics & KPI Queries
        ↓
ML Demand Model (Regression)
        ↓
FastAPI Prediction Service
        ↓
Streamlit Interactive Dashboard

This demonstrates full-stack capability:

Data Engineering → Analytics → ML → Deployment → Visualization

📊 Key Infrastructure Insights

500 EV charging stations analysed

951 total chargers nationwide

State-level infrastructure distribution

High-capacity charging hubs identified

0 missing geo records after validation

Standardized inconsistent state naming across datasets

🤖 Demand Forecasting

A baseline regression model was implemented to simulate EV charging demand trends across the year.

This demonstrates:

Time-based modeling

Model evaluation (MAE comparison)

Deployment via REST API

Real-time inference integration with dashboard

🛠️ Tech Stack
Languages & Tools

Python

SQL

Data Engineering

Pandas

PostgreSQL

SQLAlchemy

Machine Learning

Scikit-learn

API Deployment

FastAPI

Uvicorn

Visualization

Streamlit

Plotly

Matplotlib

🚀 How to Run Locally
1️⃣ Train Model
python models/train_baseline.py
2️⃣ Start FastAPI Backend
uvicorn api.app:app --reload

API runs at:

http://127.0.0.1:8000
3️⃣ Start Streamlit Dashboard
streamlit run dashboard/app.py

Dashboard runs at:

http://localhost:8501
🎯 What This Project Demonstrates

API data ingestion

ETL pipeline design

Data standardization

Database schema design

KPI computation

Forecasting model implementation

Model evaluation

REST API deployment

Frontend integration

Production-style multi-layer architecture

📈 Why This Project Matters

EV adoption is accelerating across Australia.

Infrastructure intelligence requires:

Reliable data pipelines

Clean standardized records

Infrastructure gap analysis

Demand modeling

Accessible dashboards for decision-makers

This project simulates how data engineering and machine learning can support EV infrastructure planning.

🔮 Future Improvements

State-level demand forecasting

Multi-year growth simulation

Infrastructure gap detection model

Cloud deployment (Docker / GCP / Azure)

CI/CD integration

👨‍💻 Author

Adarsh S
Master of Data Science – Deakin University
Focused on Data Engineering, ML Systems, and Applied Analytics
