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

X1=DaneArray[:, 0]
Y1=DaneArray[:, 1]
X2=DaneArray[:,2]
Y2=DaneArray[:,3]

plt.xlabel("Czas t, w sekundach")
plt.ylabel("Napiecie V, w woltach")
plt.plot(X1,Y1)
plt.plot(X2,Y2)
plt.grid()
plt.xlim(0, X1[1]*1000)
plt.savefig(NazwaPliku[:-3] + "png")
plt.show()
