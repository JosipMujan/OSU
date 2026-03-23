import matplotlib.pyplot as plt
import pandas as pd

data  = pd.read_csv("data_C02_emission.csv")

#a)
print("Broj mjerenja", len(data))
print("Tipovi velicina:\n", data.dtypes)
print("Izostale vrijednosti:\n", data.isnull().sum())
print("Duplicirane vrijednosti:\n", data.duplicated().sum())
data = data.dropna()
data = data.drop_duplicates()
data = data.reset_index(drop = True)

categorical_columns = ["Make", "Model", "Vehicle Class",
                       "Transmission", "Fuel Type"]
#bez kovertiranja kategorickig velicina u tip category, kaze ne moramo

#b)
#print(data.nlargest(3,"Fuel Consumption City (L/100km)")["Make","Model", "Fuel Consumption City (L/100km)"])
#print(data.nsmallest(...))
largest_consumption = data.sort_values(by="Fuel Consumption City (L/100km)",
                                       ascending=False).head(3)
print("\nNajveca gradska potrosnja:", largest_consumption[["Make", "Model", "Fuel Consumption City (L/100km)"]])

smallest_consumption = data.sort_values(by="Fuel Consumption City (L/100km)",
                                        ascending=False).tail(3)
print("Najveca gradska potrosnja:", smallest_consumption[["Make", "Model", "Fuel Consumption City (L/100km)"]])

#c)
motor_size = data[(data["Engine Size (L)"] >= 2.5) & (data["Engine Size (L)"] <= 3.5)]
print("Broj vozila s 2.5-3.5\n", len(motor_size))
print("Prosjecna emisija goriva\n", motor_size["CO2 Emissions (g/km)"].mean())

#d)
audi = data[data["Make"] == "Audi"]
print("\nBroj audi vozila:\n", len(audi))

audi4 = audi[audi["Cylinders"] == 4]
print("Prosjecna CO2 emisija audija s 4 cilinda\n:", audi4["CO2 Emissions (g/km)"].mean())

#e)
cylinder4 = data[data["Cylinders"] == 4]
cylinder6 = data[data["Cylinders"] == 6]
cylinder8 = data[data["Cylinders"] == 8]
cylinder10 = data[data["Cylinders"] == 10]
cylinder12 = data[data["Cylinders"] == 12]

print("4cylinder emission:", cylinder4["CO2 Emissions (g/km)"].mean())
print("6cylinder emission:", cylinder6["CO2 Emissions (g/km)"].mean())
print("8cylinder emission:", cylinder8["CO2 Emissions (g/km)"].mean())
print("10cylinder emission:", cylinder10["CO2 Emissions (g/km)"].mean())
print("12cylinder emission:", cylinder12["CO2 Emissions (g/km)"].mean())

#f)
diesel = data[data["Fuel Type"] == "D"]
regular = data[data["Fuel Type"] == "X"]
print("\nDizel potrosnja:", diesel["Fuel Consumption City (L/100km)"].median())
print("\nBenzin potrosnja:", regular["Fuel Consumption City (L/100km)"].median())

#g)
diesel4 = data[(data["Fuel Type"] == "D") &
               (data["Cylinders"] == 4)]
max_diesel4 = diesel4.sort_values(by = "Fuel Consumption City (L/100km)",
                                  ascending=False).head(1)
print("\nNajveca potrosnja dizel 4 cilindersokg motora",
      max_diesel4[["Make", "Model", "Fuel Consumption City (L/100km)"]])

#h)
manual = data[data["Transmission"].str.contains("M")]
print("\nBroj manualaca", len(manual))

#i)
print("\nKorelacija")
print(data.corr(numeric_only = True))



