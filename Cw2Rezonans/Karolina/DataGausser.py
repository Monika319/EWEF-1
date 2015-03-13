# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
rc('font', family='Consolas')


files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) and f.lower().endswith(".dat") ]
for NazwaPliku in files:
    DaneArray=np.loadtxt(NazwaPliku)
    NewDaneArray=np.copy(DaneArray)
    NewDaneArray[:,1]+=np.random.normal(0.0, 0.1, np.shape(DaneArray[:,1]))
    np.savetxt(NazwaPliku[:-4] + "_Gaussed.dat", NewDaneArray)
