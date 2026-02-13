import pandas as pd
from sklearn.metrics import mean_absolute_error

baseline = pd.read_csv("models/baseline_predictions.csv")
prophet = pd.read_csv("models/prophet_predictions.csv")

mae_baseline = mean_absolute_error(baseline["actual"], baseline["baseline_pred"])
mae_prophet = mean_absolute_error(prophet["actual"], prophet["prophet_pred"])

print("Model Comparison")
print("------------------")
print("Baseline MAE:", round(mae_baseline, 2))
print("Prophet MAE:", round(mae_prophet, 2))

if mae_prophet < mae_baseline:
    print("Prophet performs better.")
else:
    print("Baseline performs better.")