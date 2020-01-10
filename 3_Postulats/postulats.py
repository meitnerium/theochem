import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = np.exp(-(x-5)**2)
dy = 2*x-10*np.cos(x)

x2val=3.5

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel(r"$\Psi(x,0)$")
plt.show()