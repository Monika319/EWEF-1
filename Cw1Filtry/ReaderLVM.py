"""
Plot oscilloscope files from MultiSim
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
NazwaPliku=sys.argv[1]

Plik=open(NazwaPliku)
Dane=Plik.readlines()[36:]
Plik.close()

N=len(Dane)
DaneArray=np.zeros((N,4))

for i in range(len(Dane)):
    DaneArray[i]=Dane[i].split()[0:4]

np.savetxt(NazwaPliku[:-3] + "dat", DaneArray)
