import numpy as np
import matplotlib.pyplot as plt

y = np.array([12, 24, 43, 55])

plt.pie(y)
plt.show()

print("===================================================")
########################## Bar Color ##################################

y = np.array([42, 35, 11, 56, 24])
myLabels = ["Apples", "Banana", "Mango", "Cherry", "Orange"]
plt.pie(y, labels = myLabels)
plt.legend(title = "Five Fruits:")
plt.show()