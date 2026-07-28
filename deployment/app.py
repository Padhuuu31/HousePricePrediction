from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("models/house_price_model.pkl")

@app.route("/")
def home():
    return "House Price Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    values = [[
        data["bedrooms"],
        data["bathrooms"],
        data["sqft_living"],
        data["sqft_lot"],
        data["floors"],
        data["waterfront"],
        data["view"],
        data["condition"],
        data["sqft_above"],
        data["sqft_basement"],
        data["yr_built"],
        data["yr_renovated"]
    ]]

    columns = [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "waterfront",
        "view",
        "condition",
        "sqft_above",
        "sqft_basement",
        "yr_built",
        "yr_renovated"
    ]

    df = pd.DataFrame(values, columns=columns)

    prediction = model.predict(df)[0]

    return jsonify({"Predicted Price": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)