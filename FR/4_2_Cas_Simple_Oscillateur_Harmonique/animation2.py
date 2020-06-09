
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


from scipy.integrate import simps




import numpy as np
from scipy.special import eval_hermite
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

y=(x+1)/alpha
fctt=Norm*H0*np.exp(-y**2/2)
integrale=[]
for i in range(len(fct0)):
    integrale.append(fctt[i]*fctt[i])
Norm= simps(integrale, x)
fctt=fctt/np.sqrt(Norm)



y=(x)/alpha
Norm=1
H1=eval_hermite(1, x, out=None)
fct1=fct1=Norm*H1*np.exp(-y**2/2)
integrale=[]
for i in range(len(fct0)):
    integrale.append(fct1[i]*fct1[i])
Norm=simps(integrale, x)
fct1=fct1/np.sqrt(Norm)


Norm=1
H2=eval_hermite(2, x, out=None)
fct2=Norm*H2*np.exp(-y**2/2)
integrale=[]
for i in range(len(fct0)):
    integrale.append(fct2[i]*fct2[i])
Norm= simps(integrale, x)
fct2=fct2/np.sqrt(Norm)

#plt.plot(x,fct0)
#plt.plot(x,fct1)
#plt.show()

#plt.plot(x,fct2)
#E2=0*x+2.5

k=1
#L=2
#x=np.arange(-L,L,0.01)
V=0.5*k*x**2



#plt.plot(x,V,'blue')

#plt.plot([-1,1],[0.5,0.5],'black')

#plt.plot([-np.sqrt(3),np.sqrt(3)],[1.5,1.5],'black')

#plt.plot([-np.sqrt(5),np.sqrt(5)],[2.5,2.5],'black')
#plt.xlabel('x (u.a.)')
#plt.ylabel('E (u.a.)')
#plt.savefig('fct_propre.png')
#plt.show()

integrale=[]
for i in range(len(fct0)):
    integrale.append(fct0[i]*fctt[i])
#integrale=abs(fct1*fct0)
#plt.plot(x,integrale)
#plt.show()
P0 = simps(integrale, x)
print('P0 = '+str(P0))
integrale=[]
for i in range(len(fct1)):
    integrale.append(fct1[i]*fctt[i])
P1 = simps(integrale, x)
print('P1 = '+str(P1))
integrale=[]
for i in range(len(fct2)):
    integrale.append(fct2[i]*fctt[i])
P2 = simps(integrale, x)
print('P2 = '+str(P2))
print('somme = '+str(P0**2+P1**2+P2**2))
def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 0.8)
    plt.plot(x,V)
    time_text.set_text('')
    return ln,

def update(frame):
    print('t = '+str(frame)+'. xmoy = '+str(xmoy))
    xdata=x
    ydata=(np.abs(fct)**2)
    dt=2*np.pi/63
    k=int(frame/dt)
    print('frame='+str(frame)+', k = '+str(k))
    xdata2=xmoy[k]
    #print('xdata = '+str(xdata))
    ln.set_data(xdata2,0)
    ln.set_data(xdata, ydata)#,label='t = '+str(frame)+' u.a.')
    time_text.set_text('t = '+str(round(frame/(2*np.pi),2))+r' $T_{\nu}$')
    #ln.legend()

    return ln,

def calcxmoy(t):
    print(t)
    xdata, ydata = x, np.abs(fctt)**2
    xdata2=0
    xmoy = np.zeros(len(t))
    k=0
    for frame in t:
        print(frame)
        fig, ax = plt.subplots()
        plt.plot(x,V)
        time_text = ax.text(0.10, 0.9, 't = '+str(round(frame/2*np.pi,2))+r' $T_{\nu}$', transform=ax.transAxes)

        fct = P0 * np.exp(-1j * 0.5 * frame) * fct0 + P1 * np.exp(-1j * 1.5 * frame) * fct1 + P2 * np.exp(
            -1j * 2.5 * frame) * fct2
        #xmoyvec = np.zeros(len(fct),dtype=np.complex64)
        xmoyvec = np.zeros(len(fct))

        for i in range(len(fct)):
            xmoyvec[i] = np.conj(fct)[i] * x[i] * fct[i]

        xmoy[k] = simps(xmoyvec, x)
        plt.plot([xmoy[k]],[0],'ro')
        print('t = ' + str(round(frame/2*np.pi,2)) + ', xmoy = ' + str(xmoy))
        plt.plot(x, abs(np.conj(fct)*fct), 'blue')
        plt.xlabel('x (u.a.)')
        plt.ylabel('E (u.a.)')
        plt.axis([-3,3,-0.1,4])
        plt.savefig('anim/anim_'+str(k)+'.png')
        plt.close()
        k=k+1
    return xmoy

t=np.linspace(0, 2*np.pi, 64)
#print(t)
xmoy = calcxmoy(t)



print("The end")
