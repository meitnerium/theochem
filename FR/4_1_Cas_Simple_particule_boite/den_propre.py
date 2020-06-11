import numpy as np
import matplotlib.pyplot as plt

L=5
n=1
x=np.arange(0,L,0.01)
y0=0*x

E1=np.float(n)**2*np.pi**2/(2*L^2)
E1vec=0*x+E1
y1=np.sqrt(2/L)*np.sin(n*np.pi*x/L)**2+E1
n=2
E2=np.float(n)**2*np.pi**2/(2*L^2)
E2vec=0*x+E2
y2=np.sqrt(2/L)*np.sin(n*np.pi*x/L)**2+E2
n=3

E3=np.float(n)**2*np.pi**2/(2*L^2)
E3vec=0*x+E3
y3=np.sqrt(2/L)*np.sin(n*np.pi*x/L)**2+E3
n=4
E4=np.float(n)**2*np.pi**2/(2*L^2)
E4vec=0*x+E4
y4=np.sqrt(2/L)*np.sin(n*np.pi*x/L)**2+E4
n=5
E5=np.float(n)**2*np.pi**2/(2*L^2)
E5vec=0*x+E5
y5=np.sqrt(2/L)*np.sin(n*np.pi*x/L)**2+E5
plt.arrow(0, 0, 0, E3*1.05,head_width=0.1)
plt.arrow(L, 0, 0, E3*1.05,head_width=0.1)
plt.plot(x,y1,'blue')
plt.plot(x,E1vec,'black')
plt.plot(x,y2)
plt.plot(x,E2vec,'black')
plt.plot(x,y3)
plt.plot(x,E3vec,'black')
#plt.plot(x,y4)
#plt.plot(x,E4vec,'black')
#plt.plot(x,y5)
#plt.plot(x,E5vec,'black')

plt.plot(x,y0,'black')
plt.xlabel('x (u.a.)')
plt.ylabel(r'$|\Psi(x)|^2$')
plt.savefig('den_propre.png')
plt.show()