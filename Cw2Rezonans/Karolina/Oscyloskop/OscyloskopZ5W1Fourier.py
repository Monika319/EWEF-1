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
files=["real_zad5_1f.txt"]
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
    w= np.fft.rfft(Ys[0])
    #freqs = np.abs(np.fft.rfftfreq(len(Ys[1]))/DeltaT)
    freqs = np.fft.rfftfreq(len(Ys[1]))#/DeltaT
    #plt.xlim(0,3e4)
    Opis=u"Układ szeregowy\nCzęstotliwośc rezonansowa"
    Nazwa=u"Z5W1"
    plt.title(u"Transformata Fouriera sygnału wyjściowego\n"+Opis)
    plt.xlabel(u"Częstotliwość [Hz]")
    plt.ylabel(u"Amplituda")
    plt.plot(freqs,w, "-")
    plt.grid()
    plt.legend(loc="best")
##    plt.savefig(Nazwa + ".png", bbox_inches='tight')
    plt.show()

    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq /DeltaT)
    print(freq_in_hertz)



