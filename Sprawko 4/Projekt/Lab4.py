import numpy as np
import pylab as plt
from matplotlib import rc
rc('font', family='Consolas')

t1=np.linspace(0,0.10, 1000000)
odpowiedzimpulsowa=293.341*np.exp(-280795.*t1)-0.0859305*np.exp(-82.2552*t1)
plt.title(u"Odpowiedź impulsowa\n293.341 exp(-280795t) - 0.0859305 exp(-82.2552t)")
xscale=1./1000
yscale=1./1000
plt.plot(t1/xscale, odpowiedzimpulsowa/yscale)
plt.xlabel(u"Czas t [ms]")
plt.ylabel(u"Napięcie wyjściowe U2 [mV]")
plt.xlim(0/xscale, 0.1/xscale)
plt.ylim(-0.1/yscale, 0/yscale)
plt.grid()
##plt.savefig("impuls.png", bbox_inches='tight')
plt.show()
plt.clf()

t2=np.linspace(0,0.10, 1000000)
odpowiedzskokowa=-0.00104468*np.exp(-280795.*t2)+0.00104468*np.exp(-82.2552*t2)
plt.title(u"Odpowiedź skokowa\n-0.00104468 exp(-280795t) + 0.00104468 exp(-82.2552t)")
xscale=1./1000
yscale=1./1000
plt.plot(t2/xscale, odpowiedzskokowa/yscale)
plt.xlabel(u"Czas t [ms]")
plt.ylabel(u"Napięcie wyjściowe U2 [mV]")
plt.xlim(0/xscale, 0.1/xscale)
plt.ylim(0/yscale, 0.001/yscale)
plt.grid()
##plt.savefig("skok.png", bbox_inches='tight')
plt.show()
plt.clf()

omega=np.logspace(0,8,100000)
transmittance=np.abs(293.255j*omega/(2.30968e7+1j*(280877.+1j*omega)*omega))
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
