import numpy as np
import matplotlib.pyplot as plt

k=1
L=2
x=np.arange(-L,L,0.01)
V=k*x**2

plt.plot(x,V,'blue')
plt.xlabel('x (u.a.)')
plt.ylabel('E (u.a.)')
plt.savefig('pot.png')
plt.show()
