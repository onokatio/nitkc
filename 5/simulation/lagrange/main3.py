import numpy as np
import math
import matplotlib.pyplot as plt

pointnum = 5
xlist = np.array([(2/(pointnum-1))*i - 1 for i in range(pointnum)])

def fx(x):
    return pow(1+25*x**2,-1)

xpoints = xlist
ypoints = fx(xlist)

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

xlist = np.arange(-1.1,1.1,0.1)

plt.plot(xlist,zn(xlist,pointnum))

for i in range(len(xpoints)):
    plt.plot(xpoints[i],ypoints[i],marker='.')

plt.plot(xpoints[0],ypoints[0],marker='.')
plt.plot(xpoints[1],ypoints[1],marker='.')
plt.plot(xpoints[2],ypoints[2],marker='.')

plt.show()
