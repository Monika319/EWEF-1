"""
Plot oscilloscope files from MultiSim
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
NazwaPliku=sys.argv[1]

Plik=open(NazwaPliku)
Dane=Plik.readlines()[20:]
Plik.close()

N=len(Dane)
DaneArray=np.zeros((N,3))

for i in range(len(Dane)):
    DaneArray[i]=Dane[i].split()[0:3]

np.savetxt(NazwaPliku[:-3] + "dat", DaneArray)
