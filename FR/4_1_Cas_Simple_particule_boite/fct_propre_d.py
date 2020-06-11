import numpy as np
import matplotlib.pyplot as plt

Lx=5
Ly=3
nx=1
ny=1
x=np.arange(0,Lx,0.01)
y=np.arange(0,Ly,0.01)


fctx1=np.sqrt(2/Lx)*np.sin(nx*np.pi*x/Lx)
fcty1=np.sqrt(2/Ly)*np.sin(ny*np.pi*y/Ly)



xmesh=np.zeros((len(x),len(y)))
ymesh=np.zeros((len(x),len(y)))
fct11=np.zeros((len(x),len(y)))

nxval=0
nyval=0
for xval in range(len(x)):
    nyval=0

    for yval in range(len(y)):
        fct11[nxval,nyval]=fctx1[nxval]*fcty1[nyval]
        xmesh[nxval,nyval]=x[nxval]
        ymesh[nxval, nyval] = y[nyval]
        nyval=nyval+1
    nxval=nxval+1
nbins=25
leveltot = plt.MaxNLocator(nbins=nbins).tick_values(fct11.min(), fct11.max())
cf=plt.contourf(xmesh,ymesh,fct11,levels=leveltot)
plt.colorbar(cf)

plt.xlabel('x (u.a.)')
plt.ylabel('y (u.a.)')

#plt.ylabel(r'$|\Psi(x)|^2$')
#plt.plot(x,y0,'black')
plt.savefig('fct_propre2d_11.png')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

Lx=5
Ly=3
nx=2
ny=1
x=np.arange(0,Lx,0.01)
y=np.arange(0,Ly,0.01)


fctx1=np.sqrt(2/Lx)*np.sin(nx*np.pi*x/Lx)
fcty1=np.sqrt(2/Ly)*np.sin(ny*np.pi*y/Ly)



xmesh=np.zeros((len(x),len(y)))
ymesh=np.zeros((len(x),len(y)))
fct11=np.zeros((len(x),len(y)))

nxval=0
nyval=0
for xval in range(len(x)):
    nyval=0

    for yval in range(len(y)):
        fct11[nxval,nyval]=fctx1[nxval]*fcty1[nyval]
        xmesh[nxval,nyval]=x[nxval]
        ymesh[nxval, nyval] = y[nyval]
        nyval=nyval+1
    nxval=nxval+1
nbins=25
leveltot = plt.MaxNLocator(nbins=nbins).tick_values(fct11.min(), fct11.max())
cf=plt.contourf(xmesh,ymesh,fct11,levels=leveltot)
plt.colorbar(cf)

plt.xlabel('x (u.a.)')
plt.ylabel('y (u.a.)')

#plt.ylabel(r'$|\Psi(x)|^2$')
#plt.plot(x,y0,'black')
plt.savefig('fct_propre2d_21.png')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

Lx=5
Ly=3
nx=1
ny=2
x=np.arange(0,Lx,0.01)
y=np.arange(0,Ly,0.01)


fctx1=np.sqrt(2/Lx)*np.sin(nx*np.pi*x/Lx)
fcty1=np.sqrt(2/Ly)*np.sin(ny*np.pi*y/Ly)



xmesh=np.zeros((len(x),len(y)))
ymesh=np.zeros((len(x),len(y)))
fct11=np.zeros((len(x),len(y)))

nxval=0
nyval=0
for xval in range(len(x)):
    nyval=0

    for yval in range(len(y)):
        fct11[nxval,nyval]=fctx1[nxval]*fcty1[nyval]
        xmesh[nxval,nyval]=x[nxval]
        ymesh[nxval, nyval] = y[nyval]
        nyval=nyval+1
    nxval=nxval+1
nbins=25
leveltot = plt.MaxNLocator(nbins=nbins).tick_values(fct11.min(), fct11.max())
cf=plt.contourf(xmesh,ymesh,fct11,levels=leveltot)
plt.colorbar(cf)

plt.xlabel('x (u.a.)')
plt.ylabel('y (u.a.)')

#plt.ylabel(r'$|\Psi(x)|^2$')
#plt.plot(x,y0,'black')
plt.savefig('fct_propre2d_12.png')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

Lx=5
Ly=3
nx=2
ny=2
x=np.arange(0,Lx,0.01)
y=np.arange(0,Ly,0.01)


fctx1=np.sqrt(2/Lx)*np.sin(nx*np.pi*x/Lx)
fcty1=np.sqrt(2/Ly)*np.sin(ny*np.pi*y/Ly)



xmesh=np.zeros((len(x),len(y)))
ymesh=np.zeros((len(x),len(y)))
fct11=np.zeros((len(x),len(y)))

nxval=0
nyval=0
for xval in range(len(x)):
    nyval=0

    for yval in range(len(y)):
        fct11[nxval,nyval]=fctx1[nxval]*fcty1[nyval]
        xmesh[nxval,nyval]=x[nxval]
        ymesh[nxval, nyval] = y[nyval]
        nyval=nyval+1
    nxval=nxval+1
nbins=25
leveltot = plt.MaxNLocator(nbins=nbins).tick_values(fct11.min(), fct11.max())
cf=plt.contourf(xmesh,ymesh,fct11,levels=leveltot)
plt.colorbar(cf)

plt.xlabel('x (u.a.)')
plt.ylabel('y (u.a.)')

#plt.ylabel(r'$|\Psi(x)|^2$')
#plt.plot(x,y0,'black')
plt.savefig('fct_propre2d_22.png')
plt.show()
