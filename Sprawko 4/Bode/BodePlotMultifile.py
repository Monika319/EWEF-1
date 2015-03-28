# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import scipy.optimize
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator
from numpy import pi

rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

files=["EksperymentBode.txt", "SymulacjaBode.txt"]
DaneLiczbowe=[]
for NazwaPliku in files:
    print(NazwaPliku)
    Plik=open(NazwaPliku)
    Dane=Plik.readlines()[3:]
    Plik.close()

    N=len(Dane)
    M=len(Dane[0].split())
    DaneArray=np.zeros((N,M))

    for i in range(len(Dane)):
        DaneArray[i]=[j.replace(',','.') for j in Dane[i].split()]
    DaneLiczbowe.append(DaneArray)
Dane=DaneLiczbowe

Xex=Dane[0][:, 0]
Yex=10**(Dane[0][:, 1]/20.)
plt.plot(Xex, Yex, "o", label=u"Eksperyment")

Xsim=Dane[1][:, 0]
Ysim=10**(Dane[1][:, 1]/20.)
plt.plot(Xsim, Ysim, "--", label=u"Symulacja") #może "x--"?

Xtheory=np.linspace(1, 4000, 100000)
Ytheory=np.abs((-24139.9 - 293.255j*Xtheory*2*pi)/(-2.3121*10**7 - (0. + 375.572j)*Xtheory*2*pi + Xtheory*2*pi*Xtheory*2*pi))
plt.plot(Xtheory, Ytheory, "--", label=u"Teoria")

#może coś dofitować?

Opis=u"Charakterystyka częstotliwościowa"
Nazwa=u"freq"

plt.title(Opis)
plt.xlim(0, 2000)
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Moduł transmitancji")
plt.grid(which='both')
plt.legend(loc="best")
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
