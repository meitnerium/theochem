import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4,0.1)
y = np.exp(-(x-4)**2,'b')
x2 = np.arange(6,10,0.1)
y2 = np.exp(-(x2-6)**2,'b')

dy = 2*x-10*np.cos(x)

x2val=3.5

plt.plot(x,y,'b')
plt.plot(x2,y2,'b')
plt.xlabel("x")
plt.ylabel(r"$\Psi(x,0)$")
plt.show()


plt.show()