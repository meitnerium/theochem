import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite
import scipy
Kte=0.5
L=5
x=np.arange(-L,L,0.01)




Norm=1
H0=eval_hermite(0, x, out=None)
alpha=1
y=(x)/alpha
fct0=Norm*H0*np.exp(-y**2/2)
integrale=[]
for i in range(len(fct0)):
    integrale.append(fct0[i]*fct0[i])
Norm= simps(integrale, x)
fct0=fct0/np.sqrt(Norm)



Norm=1
H0=eval_hermitenorm(0, x, out=None)
alpha=1
y=x/alpha
fct0=Norm*H0*np.exp(-y**2/2)*Kte+0.5
E0=0*x+0.5


Norm=1
H1=eval_hermitenorm(1, x, out=None)
fct1=fct1=Norm*H1*np.exp(-y**2/2)*Kte+1.5

Norm=1
H2=eval_hermitenorm(2, x, out=None)
fct2=Norm*H2*np.exp(-y**2/2)*Kte+2.5
E1=0*x+1.5


plt.plot(x,fct0)
plt.plot(x,fct1)
plt.plot(x,fct2)
E2=0*x+2.5

k=1
#L=2
#x=np.arange(-L,L,0.01)
V=0.5*k*x**2


plt.plot(x,V,'blue')

plt.plot([-1,1],[0.5,0.5],'black')

plt.plot([-np.sqrt(3),np.sqrt(3)],[1.5,1.5],'black')

plt.plot([-np.sqrt(5),np.sqrt(5)],[2.5,2.5],'black')
plt.xlabel('x (u.a.)')
plt.ylabel('E (u.a.)')


plt.axis([-3,3,-0.1,4])
plt.xlabel('x (u.a.)')
plt.ylabel('E (u.a.)')
plt.savefig('fct_propre.png')
plt.show()
