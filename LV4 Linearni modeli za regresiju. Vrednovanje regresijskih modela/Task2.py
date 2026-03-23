import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

data = pd.read_csv("LV3 Upoznavanje s Pandas bibliotekom. Predobrada podataka i eksplorativna analiza podataka\data_C02_emission.csv")

#a) Task1
numerical_features = [
    'Engine Size(L)',
    'Cylinders',
    'Fuel Consumption City (L/100 km)',
    'Fuel Consumption Hwy (L/100 km)',
    'Fuel Consumption Comb (L/100 km)'
]

X = data[numerical_features]
y = data['CO2 Emissions(g/km)']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
#==================
# Task 4.5.2
#==================0
# One-hot encoding Fuel Type
ohe = OneHotEncoder(sparse=False)
fuel_encoded = ohe.fit_transform(data[['Fuel Type']])

fuel_df = pd.DataFrame(fuel_encoded, columns=ohe.get_feature_names_out(['Fuel Type']))

# novi dataset (bez skaliranja)
X2 = pd.concat([X.reset_index(drop=True), fuel_df], axis=1)

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y, test_size=0.2, random_state=42
)

model2 = LinearRegression()
model2.fit(X2_train, y2_train)

y2_pred = model2.predict(X2_test)

# maksimalna pogreška
errors = np.abs(y2_test - y2_pred)
max_error = np.max(errors)
max_index = np.argmax(errors)

print("\nModel s Fuel Type")
print("Maksimalna pogreška:", max_error)

# pronađi vozilo
vehicle = data.iloc[X2_test.index[max_index]]
print("\nVozilo s najvećom pogreškom:")
print(vehicle[['Make', 'Model', 'Vehicle Class']])