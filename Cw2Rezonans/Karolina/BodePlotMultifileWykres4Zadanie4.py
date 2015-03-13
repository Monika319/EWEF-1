# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

files = ["real_zad7_r10k_Gaussed.dat","sim_zad7_r10k.dat","real_zad7_r30k_Gaussed.dat", "sim_zad7_r30k.dat"]
Dane=[]
for NazwaPliku in files:
    Dane.append(np.loadtxt(NazwaPliku))
Xex=Dane[0][:, 0]
Yex=10**(Dane[0][:, 1]/20.)
plt.plot(Xex, Yex, "o", label=u"10k Ω eksperyment")
Xsim=Dane[1][:, 0]
Ysim=10**(Dane[1][:, 1]/20.)
plt.plot(Xsim, Ysim, "-", label=u"10k Ω symulacja")
Xex2=Dane[2][:, 0]
Yex2=10**(Dane[2][:, 1]/20.)
plt.plot(Xex2, Yex2, "o", label=u"30k Ω eksperyment")
Xsim2=Dane[3][:, 0]
Ysim2=10**(Dane[3][:, 1]/20.)
plt.plot(Xsim2, Ysim2, "-", label=u"30k Ω symulacja")


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

Opis=u"Wykres 4\nRównoległy RLC"
Nazwa=u"Wykres4"

plt.title(Opis)
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Moduł napięcia wyjściowego |U| [V]")
plt.grid(which='both')
plt.legend(loc="best")
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
