import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#==================
# Task 4.5.1
#==================

data = pd.read_csv("LV3 Upoznavanje s Pandas bibliotekom. Predobrada podataka i eksplorativna analiza podataka\data_C02_emission.csv")

#a)
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

#b)
plt.figure()
plt.scatter(X_train['Engine Size(L)'], y_train, color='blue', label='Train')
plt.scatter(X_test['Engine Size(L)'], y_test, color='red', label='Test')
plt.xlabel("Engine Size(L)")
plt.ylabel("CO2 Emissions")
plt.legend()
plt.title("Ovisnost CO2 o veličini motora")
plt.show()

#c)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# histogram prije i poslije
plt.figure()
plt.hist(X_train['Engine Size(L)'], bins=20)
plt.title("Prije skaliranja")
plt.show()

plt.figure()
plt.hist(X_train_scaled[:, 0], bins=20)
plt.title("Nakon skaliranja")
plt.show()

#d)
model = LinearRegression()
model.fit(X_train_scaled, y_train)

print("Intercept (θ0):", model.intercept_)
print("Koeficijenti (θ):", model.coef_)

#e)
y_pred = model.predict(X_test_scaled)

plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Stvarne vrijednosti")
plt.ylabel("Predikcija")
plt.title("Stvarno vs Predikcija")
plt.show()

#f)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nEvaluacija")
print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R2:", r2)

#g)
print("\nNapomena:")
print("Više ulaznih varijabli obično smanjuje grešku, ali može dovesti do overfittinga.")