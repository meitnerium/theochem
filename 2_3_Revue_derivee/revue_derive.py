import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = x**2-10*np.sin(x)
dy = 2*x-10*np.cos(x)

x2val=3.5

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axis([0,10,-12,110])
#plt.savefig("fonction.png")
#plt.show()
#plt.close()

plt.arrow(3, -20, 0, 27,length_includes_head=1,head_width=0.1,head_length=5,color='r')
x0 = plt.text(2.8, -22, '$x_0$', color='r')

plt.arrow(x2val, -20, 0, x2val**2-10*np.sin(x2val)+20,length_includes_head=1,head_width=0.1,head_length=5,color='r')
x0dx = plt.text(x2val-0.4, -22, '$x_0+\Delta x$', color='r')

x2 = np.array([3,x2val])
fx2 = x2**2-10*np.sin(x2)

xval3 = 3**2-10*np.sin(3)
xval5 = x2val**2-10*np.sin(x2val)
m = (xval5-xval3)/(x2val-3)
b = xval3-3*m

ligne = m*x+b


plt.plot(x2,fx2,'Xr')
#plt.show()
#plt.close()

plt.plot(x2,fx2,'Xr-')
#plt.show()
#plt.close()


plt.plot(x,ligne,color='black')
entetxt = plt.text(2.5, 35, '$g(x)=mx+b$', color='black')

plt.show()
plt.close()

plt.plot(x,dy)
plt.show()