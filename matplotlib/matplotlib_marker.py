import numpy as np
import matplotlib.pyplot as plt

y = np.array([3 , 8, 1, 10])

# plt.plot(y, marker = '*') with marker design
plt.plot(y, marker = 'o')
plt.show()

########## Marker Color , markersize as ms, markeredgecolor as mec ####################

y1 = np.array([3, 8, 1, 10])

plt.plot(y1, marker = 'o', ms = 20, mec = 'r')
plt.show()