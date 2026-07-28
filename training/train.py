import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create models folder
os.makedirs("models", exist_ok=True)

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_house_price.csv")

# Remove unnecessary text columns
df = df.drop(columns=["date","street","city","statezip","country"])

# Features
X = df.drop("price", axis=1)

# Target
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/house_price_model.pkl")

print("Model trained successfully!")
print("Model saved as models/house_price_model.pkl")