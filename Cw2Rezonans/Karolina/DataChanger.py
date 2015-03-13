# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
rc('font', family='Consolas')


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
