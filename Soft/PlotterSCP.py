import numpy as np
import matplotlib.pyplot as plt
import sys
NazwaPliku=sys.argv[1]
DaneArray=np.loadtxt(NazwaPliku)
X=DaneArray[:, 0]
Y1=DaneArray[:, 1]
Y2=DaneArray[:,2]

plt.xlabel("Czas t, w sekundach")
plt.ylabel("Napiecie V, w woltach")
plt.plot(X,Y1)
plt.plot(X,Y2)
plt.grid()
plt.xlim(0, X[1]*1000)
plt.savefig(NazwaPliku[:-3] + "png", bbox_inches='tight')
plt.show()
