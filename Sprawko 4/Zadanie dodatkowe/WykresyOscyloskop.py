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

NazwaPliku="ZadanieDodatkowe.txt"
print NazwaPliku
Plik=open(NazwaPliku)
Dane=Plik.readlines()
DeltaT=float(Dane[2].split()[3].replace(",","."))
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
X=np.zeros_like(Ys[0])
for i in range(len(X)):
    X[i]=i*DeltaT



plt.title(u"Zadanie dodatkowe - sweep")
plt.xlabel(u"Czas t [s]")

plt.plot(X-0.00855,Ys[0],"r-",label=u"Wejście")
plt.plot(X-0.00855,Ys[1],"b-",label=u"Wyjście")
plt.xlim(0,0.08950-0.00855)
plt.grid()
plt.legend()
plt.xlabel(u"Czas t [s]")

plt.savefig("Dodatkowe.png", bbox_inches='tight')
plt.show()



