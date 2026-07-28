import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/house_price.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("data/processed/cleaned_house_price.csv", index=False)

print("Dataset cleaned successfully!")
print("Saved as data/processed/cleaned_house_price.csv")