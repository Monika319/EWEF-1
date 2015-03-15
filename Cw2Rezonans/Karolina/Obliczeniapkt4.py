from __future__ import division

from numpy import *
f0=14553.381
Rg = 50.
C=6.2e-9
w0=2*pi*f0
L=1/w0/w0/C
print L
dane=[(33., 53.), (133.,  13.)]
for R, Q in dane:
    print R, Q
    rl=1/Q/w0/C-Rg-R
    print rl
    rl = w0*L/Q-w0**2 * C*L*(Rg+R)
    print rl
