import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 6])
y = np.array([0, 250])

plt.plot(x, y)
plt.show()



print("===================================================")
########################## Plotting Without Line ##################################

x1 = np.array([1, 8])
y1 = np.array([3, 10])

plt.plot(x1, y1, 'o')
plt.show()

########################## Multiple Points ##################################

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

x2 = np.array([1, 2, 6, 8])
y2 = np.array([3, 8, 1, 10])

plt.plot(x2, y2)
plt.show()