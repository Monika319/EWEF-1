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

fig, ax1 = plt.subplots()
ax2=ax1.twinx()

#Eksperyment
NazwaPliku="EksperymentPeak5HzInput10V+5.txt"
print NazwaPliku
Plik=open(NazwaPliku)
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
X=np.zeros_like(Ys[0])
for i in range(len(X)):
    X[i]=i*DeltaT

#AX1 - WEJŚCIE, CZERWONE
#AX2 - WYJŚCIE, NIEBIESKIE

plt.title(u"Odpowiedź impulsowa")
plt.xlabel(u"Czas t [s]")
ax1.set_ylabel(u"Napięcie wejściowe [V]", color="r")
ax2.set_ylabel(u"Napięcie wyjściowe [V]", color="b")
ein,  =ax1.plot(X,Ys[0],"r-",label=u"Eksperyment") #Eksperyment wejście
eout, = ax2.plot(X,Ys[1],"b-",label=u"Eksperyment") #Eksperyment wyjście
ax1.set_ylim(-10,10)
#Symulacja
NazwaPliku="DomowaSymulacjaPeak.scp"
Plik=open(NazwaPliku)
Dane=Plik.readlines()[19:]
Plik.close()

N=len(Dane)
DaneArray=np.zeros((N,3))

for i in range(len(Dane)):
    DaneArray[i]=Dane[i].split()[0:3]

X=DaneArray[:, 0]#-DaneArray[0,0]
Y1=DaneArray[:, 1]
Y2=DaneArray[:,2]

sin, = ax1.plot(X,Y1, "m-", label=u"Symulacja") #Symulacja wejście
sout, = ax2.plot(X,Y2, "c-", label=u"Symulacja") #Symulacja wyjście

for t1 in ax1.get_yticklabels():
    t1.set_color('r')
for t2 in ax2.get_yticklabels():
    t2.set_color('b')

#Sklejanie
plt.xlim(0,0.05)
plt.grid()
ax1.grid()
ax2.grid()
a1l=ax1.legend(loc="lower right")
a1l.set_title(u"Wejście")
a2l=ax2.legend(loc="upper right")
a2l.set_title(u"Wyjście")
ax1.set_xlabel(u"Czas t [s]")

plt.savefig("Peak.png", bbox_inches='tight')
plt.show()



