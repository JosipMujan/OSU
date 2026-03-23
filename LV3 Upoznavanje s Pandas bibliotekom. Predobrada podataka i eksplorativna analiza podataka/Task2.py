import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data_C02_emission.csv")
#a)
data["CO2 Emissions (g/km)"].plot(kind="hist", bins=20)
plt.title("Distribucija CO2 emisije")
plt.xlabel("CO2 Emissions (g/km)")


#b)
data.plot.scatter(
    x="Fuel Consumption City (L/100km)",
    y="CO2 Emissions (g/km)",
    c=data["Fuel Type"].astype("category").cat.codes,
    cmap="viridis"
)
    #c=data["Fuel Type"].map({"D": "blue", "X": "red"}),  
plt.title("Gradska potrosnja vs CO2 emisija")


#c)
data.boxplot(column="Fuel Consumption City (L/100km)",
             by = "Fuel Type")
plt.title("Gradska potrosnja po tipu goriva")


#d)
plt.figure()
fuel_counts = data.groupby("Fuel Type").size()
fuel_counts.plot(kind="bar")
plt.title("Broj vozila po tipu goriva")


#e)
plt.figure()
co2_cylinder = data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean()
co2_cylinder.plot(kind="bar")
plt.title("Prosjecna CO2 emisija po broju cilindara")

plt.tight_layout()
plt.show()