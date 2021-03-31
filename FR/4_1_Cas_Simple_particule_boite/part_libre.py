import numpy as np
import matplotlib.pyplot as plt

L=5
n=1
x=np.arange(0,L,0.01)
y0=0*x
AMP=2

E1=np.float(n)**2*np.pi**2/(2*L^2)
E1vec=0*x+E1
y1=np.sqrt(2/L)*np.sin(n*np.pi*x/L)*AMP+E1
n=2
E2=np.float(n)**2*np.pi**2/(2*L^2)
E2vec=0*x+E2
y2=np.sqrt(2/L)*np.sin(n*np.pi*x/L)*AMP+E2
n=3

E3=np.float(n)**2*np.pi**2/(2*L^2)
E3vec=0*x+E3
y3=np.sqrt(2/L)*np.sin(n*np.pi*x/L)*AMP+E3
n=4
E4=np.float(n)**2*np.pi**2/(2*L^2)
E4vec=0*x+E4
y4=np.sqrt(2/L)*np.sin(n*np.pi*x/L)*AMP+E4
n=5
E5=np.float(n)**2*np.pi**2/(2*L^2)
E5vec=0*x+E5
y5=np.sqrt(2/L)*np.sin(n*np.pi*x/L)+E5


fig, ax1 = plt.subplots()
plt.arrow(0, 0, 0, E3*1.05,head_width=0.1)
plt.arrow(L, 0, 0, E3*1.05,head_width=0.1)
plt.plot(x,E1vec,'black')
plt.plot(x,E2vec,'black')
plt.plot(x,E3vec,'black')
#plt.plot(x,y4)
#plt.plot(x,E4vec,'black')
#plt.plot(x,y5)
#plt.plot(x,E5vec,'black')
plt.xlabel('x (u.a.)')
plt.ylabel(r'E (u.a.)')
plt.plot(x,y0,'black')
plt.axis([0,L,0,13])
ax2 = ax1.twinx()
plt.plot(x,y1,'blue')
plt.plot(x,y2)
plt.plot(x,y3)

ax2ticks=[min(y1),max(y1),min(y2),max(y2),min(y3),max(y3)]
ax2tickstxt=[str(round(min(y1-E1)/AMP,2)),str(round(max(y1-E1)/AMP,2)),str(round(min(y2-E2)/AMP,2)),
             str(round(max(y2-E2)/AMP,2)),str(round(min(y3-E3)/AMP,2)),str(round(max(y3-E3)/AMP,2))]
ax2.set_yticks(ax2ticks)
ax2.set_yticklabels(ax2tickstxt)
plt.axis([0,L,0,13])
plt.ylabel(r'$|\Psi(x)|$')
plt.savefig('fct_propre.png')
plt.show()
plt.close()
fig, ax1 = plt.subplots()
plt.axis([0.1,L+0.1,0,14])
AMP2=5
plt.xlabel('x (u.a.)')
plt.ylabel(r'E (u.a.)')
plt.arrow(0, 0, 0, E3*1.15,head_width=0.1)
plt.arrow(L, 0, 0, E3*1.15,head_width=0.1)
plt.plot(x,y0,'black')
plt.plot(x,E1vec,'black')
plt.plot(x,E2vec,'black')
plt.plot(x,E3vec,'black')
ax2 = ax1.twinx()
plt.plot(x,((y1-E1)/AMP)**2*AMP2+E1)
plt.plot(x,((y2-E2)/AMP)**2*AMP2+E2)
plt.plot(x,((y3-E3)/AMP)**2*AMP2+E3)
plt.axis([0.1,L+0.1,0,14])
ax2ticks=[min(((y1-E1)/AMP)**2*AMP2+E1),max(((y1-E1)/AMP)**2*AMP2+E1),min(((y2-E2)/AMP)**2*AMP2+E2),max(((y2-E2)/AMP)**2*AMP2+E2),min(((y3-E3)/AMP)**2*AMP2+E3),max(((y3-E3)/AMP)**2*AMP2+E3)]
ax2tickstxt=[str(round(min((y1-E1)/AMP)**2,2)),str(round(max((y1-E1)/AMP)**2,2)),str(round(min((y2-E2)/AMP)**2,2)),
             str(round(max(y2-E2)/AMP,2)),str(round(min(y3-E3)/AMP,2)),str(round(max(y3-E3)/AMP,2))]
ax2.set_yticks(ax2ticks)
ax2.set_yticklabels(ax2tickstxt)

plt.savefig('den_propre.png')
plt.show()

