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

X=DaneArray[:, 0]
Y1=DaneArray[:, 1]
Y2=DaneArray[:,2]

plt.xlabel("Czas t, w sekundach")
plt.ylabel("Napiecie V, w woltach")
plt.plot(X,Y1)
plt.plot(X,Y2)
plt.grid()
plt.xlim(min(X),max(X))
plt.savefig(NazwaPliku[:-3] + "png", bbox_inches='tight')
plt.show()
