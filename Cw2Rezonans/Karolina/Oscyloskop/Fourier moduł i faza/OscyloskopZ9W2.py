# -*- coding: utf-8 -*-
"""
Plot oscilloscope files from MultiSim
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from matplotlib import rc

rc('font',family="Consolas")
files=["real_zad9_05f.txt"]
for NazwaPliku in files:
    print NazwaPliku
    Plik=open(NazwaPliku)
    #print DeltaT
    Dane=Plik.readlines()#[4:]
    DeltaT=float(Dane[2].split()[3].replace(",","."))
    #M=len(Dane[4].split())/2
    M=2
    Dane=Dane[5:]
    Plik.close()

    print M
    Ys=[np.zeros(len(Dane)) for i in range(M)]

    for m in range(M):
        for i in range(len(Dane)):
            try:
                Ys[m][i]=float(Dane[i].split()[2+3*m].replace(",","."))
            except:
                print m, i, 2+3*m, len(Dane[i].split()), Dane[i].split()
        #print i, Y[i]
    X=np.zeros_like(Ys[0])
    for i in range(len(X)):
        X[i]=i*DeltaT


    Opis=u"Układ równoległy\nPołowa częstotliwości rezonansowej"
    Nazwa=u"Z9W2"
    plt.title(u"Przebieg napięciowy\n"+Opis)
    plt.xlabel(u"Czas t [s]")
    plt.ylabel(u"Napięcie [V]")
    plt.plot(X,Ys[0],label=u"Wejście")
    plt.plot(X,Ys[1],label=u"Wyjście")
    plt.grid()
    plt.legend(loc="best")
    plt.savefig(Nazwa + ".png", bbox_inches='tight')
    plt.show()



