# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
import scipy.optimize
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

##Ysim_quality=max(Ysim)/np.sqrt(2)
##Xsim_quality=[min(Xsim),max(Xsim)]
##plt.plot(Xsim_quality, [Ysim_quality,Ysim_quality], "b-.", label=u"Punkt 1/2 mocy sym.")
##plt.plot([14007,14007], [0,Ysim_quality], "k--")
##plt.plot([15074,15074], [0,Ysim_quality], "k--")
##plt.plot([1.455459100000000035e+04,1.455459100000000035e+04], [0,max(Ysim)], "m--", label=u"f\0")
xticks=np.linspace(minx, maxx, 6)

f0=14550.

def Lorentz(f, Q, A):
    return A/np.sqrt(1.+Q*Q*(f/f0 - f0/f)**2)
popt, pcov = scipy.optimize.curve_fit(Lorentz, Xex, Yex)
perr = np.sqrt(np.diag(pcov))
print "[Q\tA]"
print popt
print perr
Xtheory=np.linspace(minx, maxx, 100000)
Ytheory=Lorentz(Xtheory, popt[0], popt[1])
plt.plot(Xtheory, Ytheory, "-", label=u"10k Ω fit Q=%.1f"%popt[0])

YsimQfactor=np.ones_like(Xtheory)*max(Ytheory)/np.sqrt(2)
##Ysimf2=14689.
##Ysimf1=14421.
##B=Ysimf2-Ysimf1
##print B
##Q=f0/B
##print Q
##print np.abs(Ysim-YsimQfactor)
##plt.plot(Xsim, np.abs(Ysim-YsimQfactor))
##plt.show()

popt, pcov = scipy.optimize.curve_fit(Lorentz, Xex2, Yex2)
perr = np.sqrt(np.diag(pcov))
print "[Q\tA]"
print popt
print perr
Xtheory=np.linspace(minx, maxx, 100000)
Ytheory=Lorentz(Xtheory, popt[0], popt[1])
plt.plot(Xtheory, Ytheory, "-", label=u"30k Ω fit Q=%.1f"%popt[0])

#plt.xscale('log')
#plt.yscale('log')
plt.xlim(minx,maxx)
plt.axes().xaxis.set_major_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_minor_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_minor_locator(FixedLocator(xticks))
plt.axes().xaxis.set_major_locator(FixedLocator(xticks))
plt.ylim(0, 1.2)

Opis=u"Wykres 5\nRównoległy RLC"
Nazwa=u"Z5W1"

plt.title(Opis)
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Moduł napięcia wyjściowego |U| [V]")
plt.grid(which='both')
plt.legend(loc="best")
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
