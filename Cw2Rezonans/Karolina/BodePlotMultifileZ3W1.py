# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

files = ["real_zad1_r30_Gaussed.dat","sim_zad1_r30.dat","real_zad1_r130_Gaussed.dat", "sim_zad1_r130.dat"]
Dane=[]
for NazwaPliku in files:
    Dane.append(np.loadtxt(NazwaPliku))
Xex=Dane[0][:, 0]
Yex=10**(Dane[0][:, 1]/20.)/33.
plt.plot(Xex, Yex, "o", label=u"33 Ω eksperyment")
Xsim=Dane[1][:, 0]
Ysim=10**(Dane[1][:, 1]/20.)/33.
plt.plot(Xsim, Ysim, "-", label=u"33 Ω symulacja")
Xex2=Dane[2][:, 0]
Yex2=10**(Dane[2][:, 1]/20.)/130.
plt.plot(Xex2, Yex2, "o", label=u"130 Ω eksperyment")
Xsim2=Dane[3][:, 0]
Ysim2=10**(Dane[3][:, 1]/20.)/130.
plt.plot(Xsim2, Ysim2, "-", label=u"130 Ω symulacja")


minx=np.round((min((min(Xsim), min(Xex)))/10000))*10000
maxx=np.round((max((max(Xsim), max(Xex)))/10000))*10000
xticks=np.linspace(minx, maxx, 6)


Ysim_quality=max(Ysim)/np.sqrt(2)
Xsim_quality=[min(Xsim),max(Xsim)]
plt.plot(Xsim_quality, [Ysim_quality,Ysim_quality], "b-.", label=u"Punkt 1/2 mocy sym.")
plt.plot([14007,14007], [0,Ysim_quality], "k--")
plt.plot([15074,15074], [0,Ysim_quality], "k--")
plt.plot([1.455459100000000035e+04,1.455459100000000035e+04], [0,max(Ysim)], "m--", label=u"f\0")
xticks=np.linspace(minx, maxx, 6)

#plt.xscale('log')
#plt.yscale('log')
plt.xlim(minx,maxx)
plt.axes().xaxis.set_major_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_minor_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_minor_locator(FixedLocator(xticks))
plt.axes().xaxis.set_major_locator(FixedLocator(xticks))

Opis=u"Zadanie 3 wykres 1\nSzeregowy RLC"
Nazwa=u"Z3W1"

plt.title(Opis)
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Moduł natężenia prądu |I| [A]")
plt.grid(which='both')
plt.legend(loc="best")
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
