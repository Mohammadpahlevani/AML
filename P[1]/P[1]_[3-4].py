# Import library
import re
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

df = pd.read_csv('206_type_2.csv', sep=',')

def remove_string(string):
    if len(string) > 15:
        return None
    return string

def remove_rows(value):
    if value == "['۱۱۱٬۱۱۱٬۱۱۱']" or value == '[]' or value == "['۰']" or value == "['۱۱٬۱۱۱٬۱۱۱']":
        return None
    return value

def remove_digit(num):
    num_str = str(num)
    if len(num_str) > 6:
        return int(num_str[1:])
    return num

df['Price(Toman)'] = df['Price(Toman)'].apply(remove_string)
df['Mileage(Kilometer)'] = df['Mileage(Kilometer)'].apply(remove_rows)
df['Model(Year)'] = df['Model(Year)'].apply(remove_rows)
df['Engine(True=Healthy)'] = df['Engine(True=Healthy)'].apply(remove_rows)
df['Chassis(True=Healthy)'] = df['Chassis(True=Healthy)'].apply(remove_rows)
df['Description(False=Expensive)'] = df['Description(False=Expensive)'].apply(remove_rows)
df['Price(Toman)'] = df['Price(Toman)'].apply(remove_rows)

df = df.dropna()

df['Price(Toman)'] = df['Price(Toman)'].map(lambda x: int(''.join(filter(str.isdigit, x))) if len(x) > 0 else None)
df['Model(Year)'] = df['Model(Year)'].map(lambda x: int(''.join(filter(str.isdigit, x))) if len(x) > 0 else None)
df['Mileage(Kilometer)'] = df['Mileage(Kilometer)'].map(lambda x: int(''.join(filter(str.isdigit, x))) if len(x) > 0 else None)
df['Mileage(Kilometer)'] = df['Mileage(Kilometer)'].apply(remove_digit)

df = df.dropna()

df = df.astype(int)

X = df[['Mileage(Kilometer)', 'Model(Year)', 'Engine(True=Healthy)', 'Chassis(True=Healthy)', 'Description(False=Expensive)']]
y = df['Price(Toman)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train.values, y_train.values)

y_pred = model.predict(X_test.values)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("R-squared:", r2)

joblib.dump(model, 'car_price_prediction_model.pkl')