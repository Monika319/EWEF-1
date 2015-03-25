import numpy as np
import pylab as plt
from matplotlib import rc
rc('font', family='Consolas')

t1=np.linspace(0,0.2, 1000000)
odpowiedzimpulsowa=np.exp(-187.786*t1)*(293.255*np.cos(4804.76*t1)-6.43723*np.sin(4804.76*t1))
plt.title(u"Odpowiedź impulsowa\nexp(-187.786t)*(293.255cos(4804.76t)-6.43723sin(4804.76t))")
xscale=1./1000
yscale=1.
plt.plot(t1/xscale, odpowiedzimpulsowa/yscale)
plt.xlabel(u"Czas t [ms]")
plt.ylabel(u"Napięcie wyjściowe U2 [V]")
plt.xlim(0/xscale, 0.02/xscale)
plt.ylim(-300/yscale, 300/yscale)
plt.grid()
plt.savefig("impuls.png", bbox_inches='tight')
plt.show()
plt.clf()

t2=np.linspace(0,0.03, 1000000)
odpowiedzskokowa=0.00104407*(1-np.exp(-187.786*t2)*np.cos(4804.76*t2))+np.exp(-187.786*t2)*0.0609935*np.sin(4804.76*t2)
plt.title(u"Odpowiedź skokowa\n0.00104407*(1-exp(-187.786t)cos(4804.76t))\n+exp(-187.786t)*0.0609935sin(4804.76t)")
xscale=1./1000
yscale=1./1000
plt.plot(t2/xscale, odpowiedzskokowa/yscale)
plt.xlabel(u"Czas t [ms]")
plt.ylabel(u"Napięcie wyjściowe U2 [mV]")
plt.xlim(0/xscale, 0.03/xscale)
plt.ylim(-0.05/yscale, 0.07/yscale)
plt.grid()
plt.savefig("skok.png", bbox_inches='tight')
plt.show()
plt.clf()

omega=np.logspace(0,8,100000)
transmittance=np.abs((-24139.9 - 293.255j*omega)/(-2.3121*10**7 - (0. + 375.572j)*omega + omega*omega))
plt.title(u"Moduł transmitancji (skala logarytmiczna)")
##xscale=1./1000
##yscale=1./1000
plt.xscale("log")
plt.yscale("log")
plt.plot(omega, transmittance)
plt.xlabel(u"Pulsacja omega [1/s]")
plt.ylabel(u"Moduł transmitancji")
##plt.xlim(0/xscale, 0.1/xscale)
##plt.ylim(0/yscale, 0.001/yscale)
plt.grid()
plt.savefig("freq.png", bbox_inches='tight')
plt.show()
plt.clf()
