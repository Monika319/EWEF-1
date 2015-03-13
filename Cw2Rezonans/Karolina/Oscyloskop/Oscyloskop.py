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

    M=2
    print M
    Ys=[np.zeros(len(Dane)) for i in range(M)]

    for m in range(M):
        #print Dane[i]
        for i in range(len(Dane)):
            try:
                Ys[m][i]=float(Dane[i].split()[2+3*m].replace(",","."))
            except:
                print m, i, 2+2*m, len(Dane[i].split()), Dane[i].split()
        #print i, Y[i]
    X=np.zeros_like(Ys[0])
    for i in range(len(X)):
        X[i]=i*DeltaT
               
    plt.title(u"Charakterystyka transmitacyjna\n"+NazwaPliku)
    plt.xlabel(u"Częstotliwość [kHz]")
    plt.ylabel(u"Wzmocnienie [dB]")
    for m in range(M):
        plt.plot(X,Ys[m],label=m)
    #plt.xlim(10,20)
    plt.grid()
    plt.legend(loc=0)
    #plt.xlim(min(X),max(X))
    plt.savefig(NazwaPliku[:-3] + "png", bbox_inches='tight')#marginesy-bbox_inches!
    plt.show()


