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
files=["real_zad9_033f.txt"]
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
    X=np.zeros_like(Ys[1])
    for i in range(len(X)):
        X[i]=i*DeltaT

    w0= np.fft.rfft(Ys[0])
    w1= np.fft.rfft(Ys[1])
    m0=np.abs(w0)
    m1=np.abs(w1)
    p0=np.angle(w0)
    p1=np.angle(w1)
    #freqs = np.abs(np.fft.rfftfreq(len(Ys[1]))/DeltaT)
    freqs = np.fft.rfftfreq(len(Ys[1]))/DeltaT
    Opis=u"Układ równoległy\nJedna trzecia częstotliwości rezonansowej"
    Nazwa=u"Z9W3Fourier"
    plt.title(u"Transformata Fouriera sygnału wyjściowego\n"+Opis)
    plt.xlabel(u"Częstotliwość [Hz]")
    plt.ylabel(u"Moduł amplitudy")
    plt.plot(freqs,m0, "-", label=u"Wejście")
    plt.plot(freqs,m1, "-", label=u"Wyjście")
    plt.xlim(0,2e5)
    plt.grid()
    plt.legend(loc="best")
    plt.savefig(Nazwa + "Modul.png", bbox_inches='tight')
    plt.show()

    plt.title(u"Transformata Fouriera sygnału wyjściowego\n"+Opis)
    plt.xlabel(u"Częstotliwość [Hz]")
    plt.ylabel(u"Przesunięcie fazowe")
    plt.plot(freqs,p0, "-", label=u"Wejście")
    plt.plot(freqs,p1, "-", label=u"Wyjście")
    plt.xlim(0,2e5)
    plt.grid()
    plt.legend(loc="best")
    plt.savefig(Nazwa + "Faza.png", bbox_inches='tight')
    plt.show()
