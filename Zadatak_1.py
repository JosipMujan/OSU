import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,3,3,2,1])
y = np.array([1,1,2,2,1])

plt.plot(x,y, 'b', linewidth = 2, marker = 'o', markersize = 5)
plt.xlabel('x os')
plt.ylabel('y os')
plt.xlim(0,4)
plt.ylim(0,4)

plt.title('Zadatak 1')
plt.show()