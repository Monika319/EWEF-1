# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

files = ["real_zad1_r130_Gaussed.dat","sim_zad1_r130.dat"]
Dane=[]
for NazwaPliku in files:
    Dane.append(np.loadtxt(NazwaPliku))
Xex=Dane[0][:, 0]
Yex=10**(Dane[0][:, 1]/20.)/130.
plt.plot(Xex, Yex, "o", label=u"Dane doświadczalne")
Xsim=Dane[1][:, 0]
Ysim=10**(Dane[1][:, 1]/20.)/130.
plt.plot(Xsim, Ysim, "-", label=u"Symulacja")


minx=np.round((min((min(Xsim), min(Xex)))/10000))*10000
maxx=np.round((max((max(Xsim), max(Xex)))/10000))*10000
xticks=np.linspace(minx, maxx, 6)

#plt.xscale('log')
#plt.yscale('log')
plt.xlim(minx,maxx)
plt.axes().xaxis.set_major_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_minor_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_minor_locator(FixedLocator(xticks))
plt.axes().xaxis.set_major_locator(FixedLocator(xticks))

Opis=u"Wykres 3\nSzeregowy RLC\nOpornik 130 Ω"
Nazwa=u"Wykres3"

plt.title(Opis)
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Moduł natężenia prądu |I| [A]")
plt.grid(which='both')
plt.legend(loc="best")
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
