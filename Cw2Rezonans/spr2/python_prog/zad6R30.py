# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc #used to customize all kinds of properties(size,dpi,color,style,etc.)
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator #do formatowania osi

rc('font', family='Consolas')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FixedLocator

files = ["zad1R30.dat","simzad1R30.dat"]
Dane=[] #empty table
for NazwaPliku in files:
    Dane.append(np.loadtxt(NazwaPliku)) #odczytuje dane z pliku tekstowego
    #0słupek w danych to f, 1 słupek to k, 2słupek to faza
Xex=Dane[0][:, 0] #dane są listą macierzy
# Dane[0]-macierz zerowa-dane x i y zczytane z pliku dla eksperymentu
# [:,0]-bierze wszystkie wiersze z kolumny 0 z 1 pliku
Yex=10**(Dane[0][:, 1]/20.)/33.
#print(max(Yex),max(Yex)/np.sqrt(2))

#wyznaczone ze wzor, log dziesiętny był!!!!
#plt.plot(Xex, Yex, "g^", label=u"Dane doświadczalne ")
# "o"-robi ciągłą linię z kropkami w punktach
# "g^"-zielone trójkąciki
# "r--" - czerwone kreski
Xsim=Dane[1][:, 0]
Ysim=10**(Dane[1][:, 1]/20.)/33.
#plt.plot(Xsim, Ysim, "-", label=u"Symulacja Q=53,7")



# "-" - wpostaci krzywej
Yex_quality=max(Yex)/np.sqrt(2)
Xex_quality=[min(Xex),max(Xex)]
#plt.plot(Xex_quality, [Yex_quality,Yex_quality], "--", label=u"Punkt 1/2 mocy eksper.")
Ysim_quality=max(Ysim)/np.sqrt(2)
Xsim_quality=[min(Xsim),max(Xsim)]
#plt.plot(Xsim_quality, [Ysim_quality,Ysim_quality], "b-.", label=u"Punkt 1/2 mocy sym.")
print(Ysim_quality)
print(Yex_quality)
f_0=1.455338100000000035e+04
Q=53.7

plt.plot(1/(1+Q**2*np.absolute(Xsim/f_0-f_0/Xsim)**2), np.absolute(Xsim/f_0-f_0/Xsim), "-", label=u"Twoja kolejność")
plt.plot(np.absolute(Xsim/f_0-f_0/Xsim), 1/(1+Q**2*np.absolute(Xsim/f_0-f_0/Xsim)**2), "-", label=u"Zamieniona kolejność")

#plt.plot([1.455338100000000035e+04,1.455338100000000035e+04], [0,max(Ysim)], "--", label=u"f_0")
#plt.plot([1.445431300000000010e+04,1.445431300000000010e+04], [0,max(Yex)], "--", label=u"f_0ex")
#lt.plot([14413,14413], [0,Ysim_quality], "k--")
#plt.plot([14684,14684], [0,Ysim_quality], "k--")
#plt.plot([14938,14938], [0,max(Yex)], "k--")


##minx=np.round((min(np.absolute(Xsim/f_0-f_0/Xsim))/10000))*10000
### zaokrąglony do całkowitych, żeby nie było liczby typu 10141..., a 10000
##maxx=np.round((max((max(np.absolute(Xsim/f_0-f_0/Xsim))/10000))*10000
##xticks=np.linspace(minx, maxx, 10)
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)[source]
#Return evenly spaced numbers over a specified interval.
#print (min((min(Xsim), min(Xex)))), minx, (max((max(Xsim), max(Xex)))), maxx, xticks
#plotuje min z min danych eksperymentalnych i symulacji

##plt.xlim(minx,maxx)
##plt.axes().xaxis.set_major_formatter(FormatStrFormatter("%d"))
##plt.axes().xaxis.set_major_locator(FixedLocator(xticks))

Opis=u"Wykres 5\nSzeregowy RLC\nOpornik 33 Ohm"
Nazwa=u"Wykres 5"

plt.title(Opis)
plt.xlabel(u"Częstotliwość f [Hz]")
plt.ylabel(u"Natężenie prądu I [A]")
plt.grid(which='both')
plt.legend(loc=1,prop={'size':10})
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
np.savetxt("zad6R30",np.transpose([1/Ysim, Xsim,np.absolute(Xsim/f_0-f_0/Xsim)]))
#np.savetxt("YexR30",np.transpose([Yex, Xex]))
