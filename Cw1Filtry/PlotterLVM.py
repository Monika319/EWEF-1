import numpy as np
import matplotlib.pyplot as plt
import sys
NazwaPliku=sys.argv[1]
DaneArray=np.loadtxt(NazwaPliku)
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
