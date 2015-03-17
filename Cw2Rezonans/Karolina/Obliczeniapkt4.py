from __future__ import division

from numpy import *
print "wszystko w SI!"
f0=14550.
df0=100
print "f0:", f0, "+-", df0
Rg = 0.
C=6.2e-9
w0=2*pi*f0
dw0=2*pi*df0

df = 50 #(błąd odczytu częstotliwości do B)
dB = sqrt(2)*df

L=1/w0/w0/C
dL=2*dw0/w0/w0/C
print "L:", L, "+-", dL
print "\n\n"

#wstawiasz opory i szerokości połówkowe B
dane=[(33., 271), (130., 1067), (1e4, 2567), (3e4, 857)]
for R, B in dane:
    print "R, B:", R, B
    Q = f0/B
    dQ=sqrt((df0/B)**2+(f0/B/B*dB)**2)
    print "Q:",Q, "+-", dQ
    rl=1/Q/w0/C-Rg-R
    drl=sqrt((L*dw0/Q)**2+(w0*dL/Q)**2+(w0*L*dQ/Q/Q)**2)
    print "r_l:",rl, "+-", drl
    Ql=w0*L/rl
    dQl = sqrt((L*dw0/rl)**2+(w0*dL/rl)**2+(w0*L*drl/rl/rl)**2)
    print "Q_l:", Ql, "+-", dQl
    print "\n\n"
