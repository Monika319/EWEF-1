from __future__ import division
import numpy as np
import pylab as plt
from matplotlib import rc
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

rc('font', family='Consolas')
R=1e2
L=1e-4
C=1e-6
w0=1/np.sqrt(L*C)
print w0
U1 = 1 #V
U2 = 0 #V (do ziemi)
colors = ['r', 'g', 'b']
Q=w0*L/R
print Q

w=np.linspace(w0/10,w0*10,1000000)
ni=w/w0-w0/w
print ni
Z=R*(1+1j*Q*ni)
I=(U1-U2)/Z
Ur=I*R
Ul=1j*w*L*I
Uc=I/(1j*w*C)
plt.plot(ni, np.abs(I), label="|I| [A]")
plt.plot(ni, np.abs(Ur), label="|Ur| [V]")
plt.plot(ni, np.abs(Ul), label="|Ul| [V]")
plt.plot(ni, np.abs(Uc), label="|Uc| [V]")
plt.grid()
plt.title(u"Zadanie 4 - układ RLC")
plt.xlabel(r"Rozstrojenie $\nu$")
plt.ylabel(u"Wielkość")
plt.legend()
plt.savefig("Zadanie4.png", bbox_inches='tight')
plt.show()
