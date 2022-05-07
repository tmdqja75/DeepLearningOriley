import numpy as np
import matplotlib.pyplot as plt

def step(x):
    return np.array(x>0, dtype=np.int8)
def sigmoid(x):
    return 1 / (1+np.exp(-x))
    
    
p = 4
x = np.arange(-p, p, 0.1)
y1 = step(x)
y2 = sigmoid(x)
plt.figure()
plt.plot(x, y1, '--')
plt.plot(x, y2, '-')
plt.ylim(-0.1, 1.1)
plt.show()