import numpy as np
import matplotlib.pyplot as plt

y = np.array([3, 8, 1, 10])

plt.plot(y, linestyle = 'dotted')
plt.show()

################################ linewidth as lw ########################################### 

y1 = np.array([3, 8, 1, 10])

plt.plot(y1, linewidth = '20.5')
plt.show()

################################ Multiple lines ########################################### 

y2 = np.array([3, 8, 1, 10])
y3 = np.array([6, 2, 8, 11])

plt.plot(y2)
plt.plot(y3)
plt.show()