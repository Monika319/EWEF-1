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




f_0=14550
Q=2.64481617e+01
plt.plot( (Xsim/f_0-f_0/Xsim),1/np.sqrt(1+Q**2*(Xsim/f_0-f_0/Xsim)**2), "-", label=u"33 Ω Teoria")
plt.plot( (Xex/f_0-f_0/Xex),Yex/1.50387323e-02, "o", label=u"33 Ω Eksperyment")


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




Q=1.06914663e+01
plt.plot( (Xsim/f_0-f_0/Xsim),1/np.sqrt(1+Q**2*(Xsim/f_0-f_0/Xsim)**2), "-", label=u"130 Ω Teoria")
plt.plot( (Xex/f_0-f_0/Xex),Yex/6.27822023e-03, "o", label=u"130 Ω Eksperyment")


Opis=u"Uniwersalna krzywa rezonansowa"
Nazwa=u"Wykres łączony"
plt.ylim(0,1.1)
plt.title(Opis)
plt.xlabel(r"Rozstrojenie względne $\nu$")
plt.ylabel(r"Unormowany moduł natężenia prądu $\ I/I_{max}$")

plt.grid(which='both')
plt.legend(loc=1,prop={'size':10})
plt.savefig(Nazwa +".png", bbox_inches='tight')
plt.show()
np.savetxt("zad6R30",np.transpose([1/Ysim, Xsim,np.absolute(Xsim/f_0-f_0/Xsim)]))
#np.savetxt("YexR30",np.transpose([Yex, Xex]))
