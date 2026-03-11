import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("data.csv", delimiter=",", skiprows = 1)

print("a) Number of persons:\n", data.shape[0])

#b) Scatter plot of height vs. weight for all persons
plt.subplot(1,2,1)
plt.scatter(data[:,1], data[:,2])
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Scatter Plot of Height vs. Weight")

#c) Scatter plot of height vs. weight for every 50th person
plt.subplot(1,2,2)
plt.scatter(data[::50,1], data[::50,2], color='red')
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Every 50th")
plt.show()

#d) Minimum, maximum and mean height
heights = data[:,1]
print("Minimum height (cm):\n", heights.min())
print("Maximum height (cm):\n", heights.max())
print("Mean height (cm):\n", heights.mean())

#e) 
men = data[:,0] == 1
height_men = data[men,1]
print("Men:")
print("Min:", np.min(height_men))
print("Max:", np.max(height_men))
print("Mean:", np.mean(height_men))

women = data[:,0] == 0
height_women = data[women, 1]
print(f"Women: min: {np.min(height_women)}, max: {np.max(height_women)}, mean: {np.mean(height_women)}")