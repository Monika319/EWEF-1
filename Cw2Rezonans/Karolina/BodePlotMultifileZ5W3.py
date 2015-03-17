# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

files = ["real_zad7_r30k_Gaussed.dat","sim_zad7_r30k.dat"]
Dane=[]
for NazwaPliku in files:
    Dane.append(np.loadtxt(NazwaPliku))
Xex=Dane[0][:, 0]
Yex=10**(Dane[0][:, 1]/20.)
plt.plot(Xex, Yex, "o", label=u"Dane doświadczalne")
Xsim=Dane[1][:, 0]
Ysim=10**(Dane[1][:, 1]/20.)
plt.plot(Xsim, Ysim, "-", label=u"Symulacja")


minx=np.round((min((min(Xsim), min(Xex)))/10000))*10000
maxx=np.round((max((max(Xsim), max(Xex)))/10000))*10000
xticks=np.linspace(minx, maxx, 6)

### "-" - w postaci krzywej
##Yex_quality=max(Yex)/np.sqrt(2)
##Xex_quality=[min(Xex),max(Xex)]
###plt.plot(Xex_quality, [Yex_quality,Yex_quality], "--", label=u"Punkt 1/2 mocy eksper.")
##Ysim_quality=max(Ysim)/np.sqrt(2)
##Xsim_quality=[min(Xsim),max(Xsim)]
##plt.plot(Xsim_quality, [Ysim_quality,Ysim_quality], "m-.", label=u"Punkt 1/2 mocy sym.")
##print(Ysim_quality)
###print(Yex_quality)

##
##plt.plot([1.455459100000000035e+04,1.455459100000000035e+04], [0,max(Ysim)], "--", label=u"f_0")
###plt.plot([1.445431300000000010e+04,1.445431300000000010e+04], [0,max(Yex)], "--", label=u"f_0ex")
##plt.plot([14125,14125], [0,Ysim_quality], "k--")
##plt.plot([14982,14982], [0,Ysim_quality], "k--")
#plt.xscale('log')
#plt.yscale('log')
plt.xlim(minx,maxx)
plt.axes().xaxis.set_major_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_minor_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_minor_locator(FixedLocator(xticks))
plt.axes().xaxis.set_major_locator(FixedLocator(xticks))

Opis=u"Wykres 7\nRównoległy RLC\nOpornik 30k Ω"
Nazwa=u"Z5W3"

plt.title(Opis)
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Moduł napięcia wyjściowego |U| [V]")
plt.grid(which='both')
plt.legend(loc="best")
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
