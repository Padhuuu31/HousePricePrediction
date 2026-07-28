import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_house_price.csv")

# Remove text columns
df = df.drop(columns=["date", "street", "city", "statezip", "country"])

# Features and target
X = df.drop("price", axis=1)
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load trained model
model = joblib.load("models/house_price_model.pkl")

# Predict
predictions = model.predict(X_test)

# Calculate R2 Score
score = r2_score(y_test, predictions)

print("\nModel Evaluation")
print("----------------------")
print("R2 Score:", score)

print("\nActual Price\tPredicted Price")
print("---------------------------------------")

for actual, predicted in zip(y_test.values[:10], predictions[:10]):
    print(f"{actual:.2f}\t{predicted:.2f}")

# Save report
with open("outputs/evaluation_report.txt", "w") as f:
    f.write(f"R2 Score = {score}\n\n")
    f.write("Actual Price\tPredicted Price\n")
    f.write("---------------------------------\n")

    for actual, predicted in zip(y_test.values[:10], predictions[:10]):
        f.write(f"{actual:.2f}\t{predicted:.2f}\n")

print("\nEvaluation report saved successfully!")