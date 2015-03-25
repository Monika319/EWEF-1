from __future__ import division
import numpy as np
import pylab as plt
from matplotlib import rc
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

rc('font', family='Consolas')
R=1e1
L=1e-4
C=1e-6
w0=1/np.sqrt(L*C)
print w0
U1 = 1 #V
U2 = 0 #V (do ziemi)
colors = ['r', 'g', 'b']

omegas=[0.5*w0, w0, 2*w0]

Dane={"I":[], "Ur":[], "Ul":[], "Uc":[]}
print Dane
for w in omegas:
    Z=R+1j*(w*L-1/w/C)
    I=(U1-U2)/Z
    Dane["I"].append(I)
    Ur=I*R
    Dane["Ur"].append(Ur)
    Ul=1j*w*L*I
    Dane["Ul"].append(Ul)
    Uc=I/(1j*w*C)
    Dane["Uc"].append(Uc)
    print w, I, Ur, Ul, Uc

#plt.figure(figsize=(6,6))
i=0
plt.title(r"""Wykres wskazowy
$\omega = \omega_{0}/2$""")
total=0j
plt.arrow(0,0,Dane["I"][i].real,Dane["I"][i].imag,fc='b', ec='b')
plt.arrow(0,0,Dane["Ur"][i].real,Dane["Ur"][i].imag,fc='g', ec='g')
plt.arrow(0,0,Dane["Ul"][i].real,Dane["Ul"][i].imag,fc='r', ec='r')
plt.arrow(0,0,Dane["Uc"][i].real,Dane["Uc"][i].imag,fc='c', ec='c')
xlimit=max((abs(min((Dane["I"][i].real, Dane["Ur"][i].real, Dane["Ul"][i].real, Dane["Uc"][i].real))), max((Dane["I"][i].real, Dane["Ur"][i].real, Dane["Ul"][i].real, Dane["Uc"][i].real))))
ylimit=max((abs(min((Dane["I"][i].imag, Dane["Ur"][i].imag, Dane["Ul"][i].imag, Dane["Uc"][i].imag))), max((Dane["I"][i].imag, Dane["Ur"][i].imag, Dane["Ul"][i].imag, Dane["Uc"][i].imag))))
limit=1.1*max((xlimit, ylimit))
plt.xlim(-limit,limit)
plt.ylim(-limit, limit)
##plt.ylim(min((Dane["I"][i].imag, Dane["Ur"][i].imag, Dane["Ul"][i].imag, Dane["Ul"][i].imag)), max((Dane["I"][i].imag, Dane["Ur"][i].imag, Dane["Ul"][i].imag, Dane["Ul"][i].imag)))
plt.xlabel(u"Część rzeczywista")
plt.ylabel(u"Część urojona")
plt.grid()
plt.savefig("polomegazero.png", bbox_inches='tight')
plt.show()    
plt.clf()

i=1
plt.title(r"""Wykres wskazowy
$\omega = \omega_{0}$""")
plt.arrow(0,0,Dane["I"][i].real,Dane["I"][i].imag,fc='b', ec='b')
plt.arrow(0,0,Dane["Ur"][i].real,Dane["Ur"][i].imag,fc='g', ec='g')
plt.arrow(0,0,Dane["Ul"][i].real,Dane["Ul"][i].imag,fc='r', ec='r')
plt.arrow(0,0,Dane["Uc"][i].real,Dane["Uc"][i].imag,fc='c', ec='c')
xlimit=max((abs(min((Dane["I"][i].real, Dane["Ur"][i].real, Dane["Ul"][i].real, Dane["Ul"][i].real))), max((Dane["I"][i].real, Dane["Ur"][i].real, Dane["Ul"][i].real, Dane["Ul"][i].real))))
ylimit=max((abs(min((Dane["I"][i].imag, Dane["Ur"][i].imag, Dane["Ul"][i].imag, Dane["Ul"][i].imag))), max((Dane["I"][i].imag, Dane["Ur"][i].imag, Dane["Ul"][i].imag, Dane["Ul"][i].imag))))
limit=1.1*max((xlimit, ylimit))
plt.xlim(-limit,limit)
plt.ylim(-limit, limit)
plt.xlabel(u"Część rzeczywista")
plt.ylabel(u"Część urojona")
plt.grid()
plt.savefig("omegazero.png", bbox_inches='tight')
plt.show()    
plt.clf()

i=2
plt.title(r"""Wykres wskazowy
$\omega = 2\omega_{0}$""")
plt.arrow(0,0,Dane["I"][i].real,Dane["I"][i].imag,fc='b', ec='b')
plt.arrow(0,0,Dane["Ur"][i].real,Dane["Ur"][i].imag,fc='g', ec='g')
plt.arrow(0,0,Dane["Ul"][i].real,Dane["Ul"][i].imag,fc='r', ec='r')
plt.arrow(0,0,Dane["Uc"][i].real,Dane["Uc"][i].imag,fc='c', ec='c')
xlimit=max((abs(min((Dane["I"][i].real, Dane["Ur"][i].real, Dane["Ul"][i].real, Dane["Ul"][i].real))), max((Dane["I"][i].real, Dane["Ur"][i].real, Dane["Ul"][i].real, Dane["Ul"][i].real))))
ylimit=max((abs(min((Dane["I"][i].imag, Dane["Ur"][i].imag, Dane["Ul"][i].imag, Dane["Ul"][i].imag))), max((Dane["I"][i].imag, Dane["Ur"][i].imag, Dane["Ul"][i].imag, Dane["Ul"][i].imag))))
limit=1.1*max((xlimit, ylimit))
plt.xlim(-limit,limit)
plt.ylim(-limit, limit)
plt.xlabel(u"Część rzeczywista")
plt.ylabel(u"Część urojona")
plt.grid()
plt.savefig("dwaomegazero.png", bbox_inches='tight')
plt.show()    
plt.clf()
