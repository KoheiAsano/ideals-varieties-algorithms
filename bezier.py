import numpy as np
import matplotlib.pyplot as plt

def weierstrass(x):
    a = 0.5
    b = 15
    N = 70
    return sum([a**i*np.cos(np.pi*b**i*x) for i in range(N)])
t = np.arange(-1.001, 1, 0.001)

plt.plot(weierstrass(t), 'b')

plt.xlabel('x')
plt.ylabel('y')
plt.title('weierstrass')
plt.show()
