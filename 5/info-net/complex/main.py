#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def dft(x,N):
    X = np.zeros(N,dtype=np.complex128)
    for k in range(len(x)):
        re=0
        im=0
        for n in range(N):
            re += x[n] * np.cos((-2*np.pi*k*n)/N)
            im += x[n] * np.sin((-2*np.pi*k*n)/N)
        X[k] = np.complex(re,im)
    return X

N=128
t = np.arange(0,N)
C=np.sin(2*np.pi*t/N*10)
C=dft(C,N)
C=np.abs(C)**2

plt.plot(t,C)
plt.show()
