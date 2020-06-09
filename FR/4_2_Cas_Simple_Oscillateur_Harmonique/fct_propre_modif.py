import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite
import scipy


from scipy.integrate import simps



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
fct0=fct0/np.sqrt(Norm)+0.5



Norm=1
H1=eval_hermite(1, x, out=None)
alpha=1
y=(x)/alpha
fct1=Norm*H1*np.exp(-y**2/2)
integrale=[]
for i in range(len(fct0)):
    integrale.append(fct1[i]*fct1[i])
Norm= simps(integrale, x)
fct1=fct1/np.sqrt(Norm)+1.5



Norm=1
H2=eval_hermite(2, x, out=None)
alpha=1
y=(x)/alpha
fct2=Norm*H2*np.exp(-y**2/2)
integrale=[]
for i in range(len(fct0)):
    integrale.append(fct2[i]*fct2[i])
Norm= simps(integrale, x)
fct2=fct2/np.sqrt(Norm)+2.5

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
plt.savefig('fct_propre_modif1.png')
plt.show()
plt.close()


plt.close()
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

E0=0*x+0.5


fctmodif=np.zeros(len(fct0))
fctmodif[0:-100]=fct0[100:]
fctmodif=fctmodif

plt.savefig('modif1.png')
plt.show()
plt.plot(x,fct0)
plt.axis([-4,4,0,0.9])
plt.plot(x,fctmodif)
plt.savefig('modif2.png')
plt.show()