import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore", category=UserWarning)

def run_predictor():
    try:
        # 1. Load data
        # Ensure 'house-prices.csv' is in the same folder as this script
        data = pd.read_csv("house-prices.csv")
    except FileNotFoundError:
        print("Error: 'house-prices.csv' not found. Please check the file path.")
        return

    # 2. Feature engineering
    features = ["SqFt", "Bedrooms", "Bathrooms"]
    target = "Price"

    # 3. Split and Train
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # 4. User input
    print("--- House Price Predictor ---")
    try:
        user_area = int(input("Enter desired area (sq ft): "))
        user_bedrooms = int(input("Enter desired number of bedrooms: "))
        user_bathrooms = int(input("Enter desired number of bathrooms: "))
        user_budget = float(input("Enter your maximum budget: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # 5. Predict price
    new_data = pd.DataFrame([[user_area, user_bedrooms, user_bathrooms]], columns=features)
    prediction = model.predict(new_data)
    # Using [0] to avoid the '0-dimensional array' error
    predicted_price = float(prediction[0])

    print(f"\nModel Predicted Price: ${predicted_price:,.2f}")

    # 6. Filtering Logic (Results show +/- 100 sq ft)
    filtered_data = data[
        (data["SqFt"] >= user_area - 100) & 
        (data["SqFt"] <= user_area + 100) &
        (data["Bedrooms"] == user_bedrooms) & 
        (data["Bathrooms"] == user_bathrooms) &
        (data["Price"] <= user_budget)
    ]

    # 7. Show Recommendations
    print("-" * 30)
    if not filtered_data.empty:
        print(f"Found {len(filtered_data)} matching houses within budget:")
        for index, row in filtered_data.iterrows():
            print(f"-> Neighborhood: {row['Neighborhood']}, Price: ${row['Price']:,.2f}, Area: {row['SqFt']} sq ft")
    else:
        print("No exact matches found in the dataset for those specs and budget.")
        print("Tip: Try increasing your budget or checking a different area size.")

if __name__ == "__main__":
    run_predictor()