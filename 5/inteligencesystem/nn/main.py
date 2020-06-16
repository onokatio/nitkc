import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=1
y=0


def sig(x):
    ips = 4
    return 1/(1+np.exp(-x * ips))

def model1_array(xy):
    x = xy[:,0]
    y = xy[:,1]
    return model1(x, y)

def model2_array(xy):
    x = xy[:,0]
    y = xy[:,1]
    return model2(x, y)

def model1(x,y):
    h1=sig((x * -1.54) + (y * 1.60) + (-0.92))
    h2=sig((x * -1.21) + (y * 1.29) + (0.58))
    o1=sig(h1 * 1.94 + h2 * -1.88 + 0.88)
    return o1

def model2(x,y):
    h1=sig((x * 0.20) + (y * 1.16) + (-1.13))
    h2=sig((x * 0.79) + (y * 0.84) + (-0.68))
    o1=sig(h1 * -1.24 + h2 * -1.55 + -0.61)
    return o1

print("model1(0,1) = ",model1(0,1))
print("model1(1,1) = ",model1(1,1))
print("model1(1,0) = ",model1(1,0))
print("model1(0,0) = ",model1(0,0))
print("model1(0.23,0.56) = ",model1(0.23,0.56))
print("model2(1,1) = ",model2(1,1))

x = np.arange(0.0,1.0,0.1)
y = np.arange(0.0,1.0,0.1)
xy = [ (a,b) for a in x for b in y ]
xy = np.array(xy)
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot(xy[:,0],xy[:,1], model1_array(xy), marker="o", linestyle='None')
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(xy[:,0],xy[:,1], model2_array(xy), marker="o", linestyle='None')
plt.show()
