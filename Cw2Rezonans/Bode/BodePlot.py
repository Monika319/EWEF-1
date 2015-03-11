# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator
files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) and f.lower().endswith(".txt") ]
for NazwaPliku in files:
    print(NazwaPliku)
    Plik=open(NazwaPliku)
    Dane=Plik.readlines()[4:]
    Plik.close()

    N=len(Dane)
    M=len(Dane[0].split())
    DaneArray=np.zeros((N,M))

    for i in range(len(Dane)):
        DaneArray[i]=[j.replace(',','.') for j in Dane[i].split()]
        #print(DaneArray[i])
    np.savetxt(NazwaPliku[:-3] + "dat", DaneArray)

    X1=DaneArray[:, 0][DaneArray[:,0] != 0]
    Y1=DaneArray[:len(X1), 1]
    X2=DaneArray[:, 3]
    Y2=DaneArray[:, 4]


    minx=min((min(X1), min(X2)))
    maxx=max((max(X2), max(X1)))
    
    plt.title(u"Charakterystyka transmitancyjna\n" + NazwaPliku)
    plt.xlabel(u"Częstotliwość f [Hz]")
    plt.ylabel(u"Wzmocnienie k [dB]")
    plt.xscale('log')
    plt.xlim(minx,maxx)
    plt.axes().xaxis.set_minor_locator(FixedLocator(np.linspace(minx,maxx, 5)))
    plt.axes().xaxis.set_major_formatter(FormatStrFormatter(""))
    plt.axes().xaxis.set_minor_formatter(FormatStrFormatter("%d"))
    plt.plot(X1,Y1, "bo", label=u"Dane doświadczalne")
    ##plt.errorbar(f, kdb, xerr=10, yerr=2)
    plt.plot(X2, Y2, "ro", label=u"Symulacja")
    plt.grid(which='both')
    #plt.legend(loc="lower right")
    plt.legend(loc="best")
    plt.show()

    #PARAMETRY DO USTAWIENIA
    minx=float(input("Min x:"))
    maxx=float(input("Max x:"))
    miny=float(input("Min y:"))
    maxy=float(input("Max y:"))
    Opis=eval("u" + input("Opis:"))

    xticks=np.linspace(minx, maxx, 6)

    plt.title(u"Charakterystyka transmitancyjna\n" + Opis)
    plt.xlabel(u"Częstotliwość f [Hz]")
    plt.ylabel(u"Wzmocnienie k [dB]")
    plt.xscale('log')

    plt.xlim(minx,maxx)
    plt.axes().xaxis.set_major_formatter(FormatStrFormatter(""))
    plt.axes().xaxis.set_minor_formatter(FormatStrFormatter("%d"))
    plt.axes().xaxis.set_minor_locator(FixedLocator(xticks))
    plt.ylim(miny,maxy)
    plt.plot(X1,Y1, "bo", label=u"Dane doświadczalne")
    ##plt.errorbar(f, kdb, xerr=10, yerr=2)
    plt.plot(X2, Y2, "ro", label=u"Symulacja")
    plt.grid(which='both')
    #plt.legend(loc="lower right")
    plt.legend(loc="best")
    plt.savefig(Opis +".png", bbox_inches='tight')
    plt.show()
