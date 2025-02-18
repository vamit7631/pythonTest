import numpy as np
import matplotlib.pyplot as plt

# plot 1

x = np.array([4, 2, 6, 8])
y = np.array([1, 7, 10, 2])


# plt.subplot(2, 1, 1)  for two rows
plt.subplot(1, 2, 1) # for two columns
plt.grid()
plt.plot(x, y)

# plot 1

x = np.array([6, 12, 4, 5])
y = np.array([10, 4, 20, 12])

# plt.subplot(2, 1, 2)  for two rows
plt.subplot(1, 2, 2) # for two columns
plt.grid()
plt.plot(x, y)


plt.suptitle("MY SHOP")
plt.show()