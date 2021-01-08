import numpy as np
import math
import matplotlib.pyplot as plt

xpoints = [1,3,4]
ypoints = [1,2,5]

def zn(x,n):
    sum = 0
    for i in range(n):
        sum = sum + z(x,i,n)
    return sum

def z(x,a,n):
    upper = 1
    downer = 1
    for i in range(n):
        if i == a:
            continue
        upper = upper * (x - xpoints[i])
        downer = downer * (xpoints[a] - xpoints[i])
    ret = ypoints[a] * (upper / downer)
    return ret

xlist = np.arange(-1,5,0.1)

plt.plot(xlist,zn(xlist,3))

plt.plot(xpoints[0],ypoints[0],marker='.')
plt.plot(xpoints[1],ypoints[1],marker='.')
plt.plot(xpoints[2],ypoints[2],marker='.')

plt.show()
