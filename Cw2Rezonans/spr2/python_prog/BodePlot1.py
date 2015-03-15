# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc #used to customize all kinds of properties(size,dpi,color,style,etc.)
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator #do formatowania osi

rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

files = ["zad1R130.dat","simzad1R130.dat"]
Dane=[] #empty table
for NazwaPliku in files:
    Dane.append(np.loadtxt(NazwaPliku)) #odczytuje dane z pliku tekstowego
    #0słupek w danych to f, 1 słupek to k, 2słupek to faza
Xex=Dane[0][:, 0] #dane są listą macierzy
# Dane[0]-macierz zerowa-dane x i y zczytane z pliku dla eksperymentu
# [:,0]-bierze wszystkie wiersze z kolumny 0 z 1 pliku
Yex=10**(Dane[0][:, 1]/20.)/133.
#print(max(Yex),max(Yex)/np.sqrt(2))

#wyznaczone ze wzor, log dziesiętny był!!!!
plt.plot(Xex, Yex, "g^", label=u"Dane doświadczalne ")
# "o"-robi ciągłą linię z kropkami w punktach
# "g^"-zielone trójkąciki
# "r--" - czerwone kreski
Xsim=Dane[1][:, 0]
Ysim=10**(Dane[1][:, 1]/20.)/133.
plt.plot(Xsim, Ysim, "-", label=u"Symulacja Q=13,64")



# "-" - w postaci krzywej
Yex_quality=max(Yex)/np.sqrt(2)
Xex_quality=[min(Xex),max(Xex)]
#plt.plot(Xex_quality, [Yex_quality,Yex_quality], "--", label=u"Punkt 1/2 mocy eksper.")
Ysim_quality=max(Ysim)/np.sqrt(2)
Xsim_quality=[min(Xsim),max(Xsim)]
plt.plot(Xsim_quality, [Ysim_quality,Ysim_quality], "b-.", label=u"Punkt 1/2 mocy sym.")
print(Ysim_quality)
#print(Yex_quality)


#plt.plot([1.455338100000000035e+04,1.455338100000000035e+04], [0,max(Ysim)], "--", label=u"f_0")
#plt.plot([1.445431300000000010e+04,1.445431300000000010e+04], [0,max(Yex)], "--", label=u"f_0ex")
plt.plot([14007,14007], [0,Ysim_quality], "k--")
plt.plot([15074,15074], [0,Ysim_quality], "k--")
plt.plot([1.455459100000000035e+04,1.455459100000000035e+04], [0,max(Ysim)], "m--", label=u"f\0")


minx=np.round((min((min(Xsim), min(Xex)))/10000))*10000
# zaokrąglony do całkowitych, żeby nie było liczby typu 10141..., a 10000
maxx=np.round((max((max(Xsim), max(Xex)))/10000))*10000
xticks=np.linspace(minx, maxx, 6)
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)[source]
#Return evenly spaced numbers over a specified interval.
#print (min((min(Xsim), min(Xex)))), minx, (max((max(Xsim), max(Xex)))), maxx, xticks
#plotuje min z min danych eksperymentalnych i symulacji

plt.xlim(minx,maxx)
plt.axes().xaxis.set_major_formatter(FormatStrFormatter("%d"))
plt.axes().xaxis.set_major_locator(FixedLocator(xticks))

Opis=u"Wykres 1\nSzeregowy RLC\nOpornik 133 Ohm"
Nazwa=u"Wykres 2"

plt.title(Opis)
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Natężenie prądu I [A]")
plt.grid(which='both')
plt.legend(loc=1,prop={'size':10})
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
np.savetxt("YsimR130",np.transpose([Ysim, Xsim]))
np.savetxt("YexR130",np.transpose([Yex, Xex]))
