import joblib

model = joblib.load('car_price_prediction_model.pkl')

mileage = int(input("Mileage (Kilometer): "))
model_year = int(input("Model (Solar year): "))
engine = int(input("Engine (Healthy=1): "))
chassis = int(input("Chassis (Healthy=1): "))
description = int(input("Description (Expensive=0): "))

features = [[mileage, model_year, engine, chassis, description]]

from termcolor import colored

predicted_price = model.predict(features)
formatted_price = "{:,.0f}".format(predicted_price[0])

print("Predicted Price:", colored(formatted_price, 'green'))