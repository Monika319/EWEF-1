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

plt.title(u"""Wykres wskazowy - napięcia
Cewka L2, 10 kHz,  θ=85,39°, ESR=87,52Ω""")
plt.xlim(-5/5, 95/5)
plt.ylim(-10/5, Im*1.05/5)
plt.xlabel(u"Część rzeczywista")
plt.ylabel(u"Część urojona")

plt.arrow(0,0,ESR/5,0,fc='b', ec='c')
plt.arrow(ESR/5,0,0,Im/5,fc='g', ec='y')
plt.arrow(0,0,ESR/5,Im/5,fc='r', ec='k')
frame = plt.gca()
plt.grid()
frame.axes.get_xaxis().set_ticklabels([])
frame.axes.get_yaxis().set_ticklabels([])
plt.savefig("zwojnicanapiecia.png", bbox_inches='tight')
plt.show()    

plt.clf()
