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
files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) and f.lower().endswith(".txt") ]
#files=["Pomiar5CzF.txt"]
for NazwaPliku in files:
    print NazwaPliku
    Plik=open(NazwaPliku)
    #print DeltaT
    Dane=Plik.readlines()#[4:]
    DeltaT=float(Dane[2].split()[3].replace(",","."))
    Dane=Dane[5:]
    Plik.close()
    Y=np.zeros(len(Dane))
    for i in range(len(Dane)):
        Y[i]=float(Dane[i].split()[2].replace(",","."))
    X=np.zeros_like(Y)
    for i in range(len(X)):
        X[i]=i*DeltaT

    plt.title(u"Charakterystyka transmitacyjna\n"+NazwaPliku)
    plt.xlabel(u"Częstotliwość [kHz]")
    plt.ylabel(u"Wzmocnienie [dB]")
    plt.plot(X,Y,"g-",label="Dane eksperymentalne")
    #plt.xlim(10,20)
    plt.grid()
    plt.legend(loc=0)
    #plt.xlim(min(X),max(X))
    plt.savefig(NazwaPliku[:-3] + "png", bbox_inches='tight')#marginesy-bbox_inches!
    plt.show()


