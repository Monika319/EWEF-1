# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='Consolas')
f=np.array([100,
300,
500,
700,
900,
1000,
1100,
1130,
1200,
1300,
1500,
1800,
2000,
3000,
4000,
6000,
10000,
100000])

Vpp=np.array([0.51,
1.37,
2.05,
2.73,
3.20,
3.37,
3.54,
3.59,
3.67,
3.80,
4.01,
4.27,
4.35,
4.65,
4.78,
4.87,
4.91,
4.95])
kdb=20*np.log10(Vpp/5.064)

R=3000
C=4.7e-8
pi=np.pi
fsource=np.linspace(10,1e6,10000)
ktheory=20*np.log10(R*C*2*pi*fsource/np.sqrt(1+(R*C*2*pi*fsource)**2))

plt.title(u"Charakterystyka transmitancyjna\nFiltr górnoprzepustowy")
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Wzmocnienie k [dB]")
plt.xscale('log')
plt.xlim(10,10**6)
plt.ylim(-25,5)
plt.plot(f,kdb, "bo", label=u"Dane doświadczalne")
#plt.errorbar(f, kdb, xerr=10, yerr=2)
plt.plot(fsource, ktheory, "c-", label=u"Charakterystyka teoretyczna")
plt.grid()
plt.legend(loc="lower right")
plt.savefig("wykres.png", bbox_inches='tight')
plt.show()
