# -*- coding: utf-8 -*-
"""
Plot oscilloscope files from MultiSim
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from matplotlib import rc

rc('font',family="Arial")
#files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) and f.lower().endswith(".scp") ]
files=["Pomiar1BodeOpornik33Ohm.txt"]
for NazwaPliku in files:
    Plik=open(NazwaPliku)
    Dane=Plik.readlines()[4:]
    Plik.close()
    N=len(Dane)
    M=len(Dane[0].split())      #dane to wiersze, dane[0] to pierwszy wiersz, split daje elementy pierwszego wiersza, ich liczba rowna sie liczbie kolumn :)
    DaneArray=np.zeros((N,M))

    for i in range(len(Dane)):
        DaneArray[i]=Dane[i].replace(",",".").split()
        print DaneArray[i]

    np.savetxt(NazwaPliku[:-3] + "dat", DaneArray)

    X1=DaneArray[:, 0][DaneArray[:, 0] !=0] /1000.#bool na true wychodzi wtedy kiedy element kolumny nie jest zerem, i to wchodzi jako indeks
    Y1=DaneArray[:, 1][DaneArray[:, 0] !=0]
    X2=DaneArray[:, 3]/1000.
    Y2=DaneArray[:, 4]
    print X1, Y1, X2, Y2
    plt.title(u"Charakterystyka transmitacyjna\n")#+NazwaPliku)
    plt.xlabel(u"Częstotliwość [kHz]")
    plt.ylabel(u"Wzmocnienie [dB]")
    plt.plot(X1,Y1,"go-",label="Dane eksperymentalne")
    plt.plot(X2,Y2,"bo",label="Dane teoretyczne")
    #plt.xlim(10,20)
    plt.grid()
    plt.legend(loc=0)
    #plt.xlim(min(X),max(X))
    plt.savefig(NazwaPliku[:-3] + "png", bbox_inches='tight')#marginesy-bbox_inches!
    plt.show()

