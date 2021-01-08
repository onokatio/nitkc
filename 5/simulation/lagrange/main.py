import numpy as np
import math
import matplotlib.pyplot as plt

x1 = 1
y1 = 1

x2 = 3
y2 = 2

x3 = 4
y3 = 5

def z1(x):
    return y1 * ( ((x-x2)*(x-x3)) / ((x1-x2)*(x1-x3)) )

def z2(x):
    return y2 * ( ((x-x1)*(x-x3) / (x2-x1)*(x2-x3)) )

def z3(x):
    return y3 * ( ((x-x1)*(x-x2) / (x3-x1)*(x3-x2)) )

def f(x):
    return z1(x) + z2(x) + z3(x)
 
xlist = np.arange(-1,5,0.01)

plt.plot(xlist,f(xlist))

plt.plot(x1,y1,marker='.')
plt.plot(x2,y2,marker='.')
plt.plot(x3,y3,marker='.')

plt.show()
