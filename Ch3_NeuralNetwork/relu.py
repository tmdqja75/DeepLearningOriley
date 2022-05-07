import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

p = 4
x = np.arange(-p, p, 0.1)
y1 = relu(x)

plt.figure()
plt.plot(x, y1, '-')
plt.ylim(-0.1, p+0.1)
plt.show()