import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
L=20
n=1
x=np.linspace(-L,L,1000,endpoint=True)
x1=np.linspace(-L,0,500,endpoint=True)
x2=np.linspace(0,L,500,endpoint=True)
dk=2*np.pi/(x[1]-x[0])
p=np.arange(0,dk*len(x),dk)
# https://demonstrations.wolfram.com/WavepacketForAFreeParticle/
# https://demonstrations.wolfram.com/EvolutionOfAGaussianWavePacket/#more
def a(deltap,t):
    # a[\[CapitalDelta]p_, t_] := 1/(4 (\[CapitalDelta]p)^2) + I t/2;
    return 1/(4*deltap**2.0) + 1j*t/2.0

def b(p0,deltap,x):
    #b[p0_, \[CapitalDelta]p_, x_] := p0/(2 (\[CapitalDelta]p)^2) + I x;
    return p0**2.0/(2*deltap**2.0) + 1j*x

def c(p0, deltap):
    #c[p0_, \[CapitalDelta]p_] := -((p0^2)/(  4 (\[CapitalDelta]p)^2)) (*Auxiliary quantities*)
    return -p0**2.0/(4.0*deltap**2.0)

def psi(p0,deltap,x,t):
#\[CapitalPsi][p0_, \[CapitalDelta]p_, x_,
#  t_] := (2 \[Pi] (\[CapitalDelta]p)^2 4 a[\[CapitalDelta]p,
#       t]^2)^(-1/4) (E^(
#  c[p0, \[CapitalDelta]p] +
#   b[p0, \[CapitalDelta]p,
#      x]^2/(4 a[\[CapitalDelta]p,
#       t]))) (*Wave packet corresponding to an initial Gaussian \
#wavefunction*)
    return (2*np.pi*deltap**2.0*4*a(deltap,t)**2.0)**0.25*np.exp(c(p0,deltap)+b(p0,deltap,x)**2.0/(4*a(deltap,t)))

def autrepsi(sigma0,p0,x,t):
    norm = (sigma0/np.sqrt(2*np.pi))**(0.5)*(sigma0**2+1j*t/2)**(-0.5)
    psi1 = np.exp(-sigma0**2*p0**2)*np.exp(-(x-2*1j*sigma0**2*p0)**2/(4*(sigma0**2+1j*t/2)))
    return norm*psi1

tvec = np.arange(0,100,0.1)
#for t in tvec:
#    plt.plot(x,np.abs(psi(0,0.1,x,t))**2.0)
#    plt.show()


from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

#x = np.linspace(-2, 2, 200)

duration = 40

fig, ax = plt.subplots()
ax.clear()
ax.plot(x, np.abs(autrepsi(2, 0, x, 0)) ** 2.0)
ax.set_ylim(0, np.abs(autrepsi(2, 0, 0, 0)) ** 2.0 * 1.05)
plt.xlabel("X")
plt.ylabel(r'$\Psi(x,0)^2$')
plt.savefig("psi_init_x.png")
plt.close()
fig, ax = plt.subplots()
ax.clear()
ax.plot(x, np.abs(autrepsi(2, 0, x, 0)) ** 2.0)
ax.set_ylim(0, np.abs(autrepsi(2, 0, 0, 0)) ** 2.0 * 1.05)
plt.xlabel("P")
plt.ylabel(r'$\Psi(p,0)^2$')
plt.savefig("psi_init_p.png")
plt.close()
fig, ax = plt.subplots()
fig, ax = plt.subplots()
ax.clear()
ax.plot(x, np.abs(autrepsi(2, 0, x, 0)) ** 2.0)
ax.set_ylim(0, np.abs(autrepsi(2, 0, 0, 0)) ** 2.0 * 1.05)
f1 = autrepsi(2, 0, x1, 0)
f2 = autrepsi(2, 0, x2, 0)
plt.xlabel("P")
plt.ylabel(r'$\Psi(p,0)^2$')
plt.fill_between(x1,np.abs(f1)**2,facecolor='red')
plt.fill_between(x2,np.abs(f2)**2,facecolor='green')
plt.savefig("psi_init_p_color.png")
plt.close()
plt.style.use('dark_background')
fig, ax = plt.subplots()

def make_frame(t):

    ax.clear()
    ax.plot(x, np.abs(autrepsi(2,0,x,5*t))**2.0)
    ax.set_ylim(0,np.abs(autrepsi(2,0,0,0))**2.0*1.05)
    ax.set_xlabel('X')
    ax.set_ylabel(r'$|\Psi(x)|^2$')
    #ax.set_title("'dark_background' style sheet")
    return mplfig_to_npimage(fig)

animation = VideoClip(make_frame, duration=duration)
animation.write_gif('matplotlib.gif', fps=20)
animation.write_videofile("my_animation.mp4", fps=20, threads=4)

#def function(x,alpha):
#    f = 1/(np.sqrt(alpha*np.pi))*np.exp(-(x**2.0)/alpha)
#    return f
#def function2(x,alpha):
#    return function(x,alpha)**2.0
#alpha = np.arange(0.1,5,0.1)
#for i in range(len(alpha)):
#    y1 = function(x,alpha[i])

#    fig, ax1 = plt.subplots()
#    plt.plot(x,y1,'blue')
#    ax.fill_between(x, 0, y1)
#    plt.xlabel("x")
#    plt.ylabel(r"$\Psi(x,t)^2$")
#    plt.axis([-7,7,0,2])
#    plt.show()
#    plt.close()
#alpha = np.arange(5.1,25,1)
#for i in range(len(alpha)):
#    y1 = function(x,alpha[i])

#    fig, ax1 = plt.subplots()
#    plt.plot(x,y1,'blue')
#    plt.xlabel("x")
#    plt.ylabel(r"$\Psi(x,t)^2$")
#    plt.axis([-7,7,0,2])
#    plt.show()
#    plt.close()
#y3 = np.fft.fftshift(np.fft.fft(y1))
#fig, ax1 = plt.subplots()
#plt.plot(x,np.abs(y3/np.sqrt(len(x)))**2.0,'blue')
#plt.axis([1.8,2.1,0,8000])
#plt.xlabel("p")
#plt.ylabel(r"$\Psi(p,t)^2$")
#plt.axis([-1,1,0,2.55])
#plt.show()
#plt.close()



#res, err = quad(function, -L, L)
#print('norm: ', str(res))