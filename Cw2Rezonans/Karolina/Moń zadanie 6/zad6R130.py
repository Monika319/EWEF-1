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
Yex=10**(Dane[0][:, 1]/20.)/130.
#print(max(Yex),max(Yex)/np.sqrt(2))

#wyznaczone ze wzor, log dziesiętny był!!!!
#plt.plot(Xex, Yex, "g^", label=u"Dane doświadczalne ")
# "o"-robi ciągłą linię z kropkami w punktach
# "g^"-zielone trójkąciki
# "r--" - czerwone kreski
Xsim=Dane[1][:, 0]
Ysim=10**(Dane[1][:, 1]/20.)/130.
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
Q=13.64

plt.plot( (Xsim/f_0-f_0/Xsim),1/np.sqrt(1+Q**2*(Xsim/f_0-f_0/Xsim)**2), "-", label=u"Krzywa teoretyczna")
plt.plot( (Xex/f_0-f_0/Xex),Yex/max(Yex), "o", label=u"Krzywa doświadczalna")
Opis=u"Szeregowy RLC\nOpornik 130 Ohm"
Nazwa=u"Wykres 6"
plt.ylim(0,1.1)
plt.title(Opis)
plt.xlabel(r"Rozstrojenie względne $\nu$")
plt.ylabel(r"Unormowany moduł natężenia prądu $\ I/I_{max}$")
plt.grid(which='both')
plt.legend(loc=1,prop={'size':10})
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
np.savetxt("zad6R130",np.transpose([1/Ysim, Xsim,np.absolute(Xsim/f_0-f_0/Xsim)]))
#np.savetxt("YexR30",np.transpose([Yex, Xex]))
