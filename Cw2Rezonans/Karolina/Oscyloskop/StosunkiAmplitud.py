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
files=["real_zad5_1f.txt", "real_zad5_05f_p2.txt", "real_zad5_033f.txt", "real_zad9_1f.txt", "real_zad9_05f.txt", "real_zad9_033f.txt"]
dane=np.zeros((len(files), 2))
for FileIndex, NazwaPliku in enumerate(files):
    print NazwaPliku
    Plik=open(NazwaPliku)
    #print DeltaT
    Dane=Plik.readlines()#[4:]
    DeltaT=float(Dane[2].split()[3].replace(",","."))
    #M=len(Dane[4].split())/2
    M=2
    Dane=Dane[5:]
    Plik.close()

    Ys=[np.zeros(len(Dane)) for i in range(M)]

    for m in range(M):
        for i in range(len(Dane)):
            try:
                Ys[m][i]=float(Dane[i].split()[2+3*m].replace(",","."))
            except:
                print m, i, 2+3*m, len(Dane[i].split()), Dane[i].split()
        #print i, Y[i]

    print max(Ys[0])-min(Ys[0])
    dane[FileIndex, 0] = max(Ys[0])-min(Ys[0])
    print max(Ys[1])-min(Ys[1])
    dane[FileIndex, 1] = max(Ys[1])-min(Ys[1])
print dane
print "szeregowy"
stosunkiszeregowy=dane[1:3,1]/dane[0,1]
print stosunkiszeregowy
stosunkiteor=np.array([0, 1/3.])
print stosunkiszeregowy-stosunkiteor
print "rownolegly"
stosunkirownolegly=dane[4:6,1]/dane[3,1]
print stosunkirownolegly
print stosunkirownolegly-stosunkiteor
