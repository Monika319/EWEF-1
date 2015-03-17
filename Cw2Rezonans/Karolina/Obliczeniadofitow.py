from __future__ import division

from numpy import *
print "wszystko w SI!"
f0=14550.
df0=100
print "f0:", f0, "+-", df0
C=6.2e-9
w0=2*pi*f0
dw0=2*pi*df0

df = 50 #(błąd odczytu częstotliwości do B)
dB = sqrt(2)*df

L=1/w0/w0/C
dL=2*dw0/w0/w0/w0/C
print "L:", L, "+-", dL
print "\n\n"

Rg=0 #wtórnik
#wstawiasz opory, dobroci i ich błędy
dane=[(33., 2.64481617e+01, 3.09522850e-01), (130., 1.06914663e+01, 1.51164595e-01)]
for R, Q, dQ in dane:
    print "R:", R
    print "Q:",Q, "+-", dQ
    rl=1/Q/w0/C-Rg-R
    drl=sqrt((L*dw0/Q)**2+(w0*dL/Q)**2+(w0*L*dQ/Q/Q)**2)
    print "r_l:",rl, "+-", drl
    Ql=w0*L/rl
    dQl = sqrt((L*dw0/rl)**2+(w0*dL/rl)**2+(w0*L*drl/rl/rl)**2)
    print "Q_l:", Ql, "+-", dQl
    print "\n\n"

##Rg=50
##dane=[(1e4, 5.27268211252, 0.0282187840119), (3e4, 12.9617327208, 0.0665328450708)]
##for R, Q, dQ in dane:
##    print "R:", R
##    print "Q:",Q, "+-", dQ
##    #print 1/Q, 1/(w0*C*Rg)
##    Ql=1/(1/Q-1/(w0*C*Rg))
##    dQl1= dQ/(1-Q/C/Rg/w0)**2
##    dQl2=dw0*C*Q*Q*Rg/(Q-C*Rg*w0)**2
##    dQl=sqrt(dQl1**2+dQl2**2)
##    #drl=sqrt((L*dw0/Q)**2+(w0*dL/Q)**2+(w0*L*dQ/Q/Q)**2)
##    print "Ql:",Ql, "+-", dQl
####    Ql=w0*L/rl
####    dQl = sqrt((L*dw0/rl)**2+(w0*dL/rl)**2+(w0*L*drl/rl/rl)**2)
####    print "Q_l:", Ql, "+-", dQl
##    print "\n\n"


f0prime=10320
C2ratio=f0*f0/f0prime/f0prime-1
C2=C*C2ratio
print "frequency ratio, C2:", f0prime/f0,C2ratio, C2
