from __future__ import division
import numpy as np
import pylab as plt
from matplotlib import rc
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

rc('font', family='Consolas')
ESR=87.52
Deg=85.39
Im=ESR*np.tan(np.pi*Deg/180.)

#plt.figure(figsize=(6,6))
plt.title(u"""Wykres wskazowy - impedancja
Cewka L2, 10 kHz,  θ=85,39°, ESR=87,52Ω""")
plt.arrow(0,0,ESR,0,fc='b', ec='b')
plt.arrow(ESR,0,0,Im,fc='g', ec='g')
plt.arrow(0,0,ESR,Im,fc='r', ec='r')
plt.xlim(-5, 95)
plt.ylim(-10, Im*1.05)
plt.xlabel(u"Część rzeczywista")
plt.ylabel(u"Część urojona")
plt.grid()
plt.savefig("zwojnica.png", bbox_inches='tight')
plt.show()    

plt.clf()
