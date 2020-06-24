#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import random

data = [random.randrange(0,2) for i in range(1024)]
data = np.reshape(data, (-1, 1) )

def NORMAL(data):
    return data * [1,1,1,1]

def NRZ(data):
    return data * [-1,-1,-1,-1]

def NRZ2(data):
    return data * [-2,-2,-2,-2] + [1,1,1,1]

def RZ(data):
    return data * [0,-1,-1,0]

def RZ2(data):
    return (data * [-1,-1,-1,-1] + [1,1,1,1]) * [0,1,1,0] + RZ(data)

def AMI(data):
    count = []
    invert = 0
    data2 = []
    for index, bit in enumerate(data):
        if bit[0] == 1:
            invert = (invert + 1)%2
            data2.append([1+invert*-2,1+invert*-2,0,0])
        else:
            data2.append([0,0,0,0])
    return np.array(data2)

def MAN(data):
    return (data * [-1,-1,-1,-1] + [1,1,1,1]) * [-1,-1,1,1] + data * [1,1,-1,-1]

def graphdata(data):
    for bits in data:
        for bit in bits:
            if bit:
                print("￣", end="")
            else:
                print("＿", end="")
        print(" ", end="")
    print("")

print(data)
print(NRZ(data))
print(NRZ2(data))
print(RZ(data))
print(RZ2(data))
print(AMI(data))
print(MAN(data))


def plotwave(fig, pos, data, title):
    width = 25
    data = data[0:width+1]
    ax1 = fig.add_subplot(pos)
    ax1.set_title(title)
    ax1.set_xticks(np.arange(0, (width+1)*4, 4), minor=False)
    ax1.set_xticks(np.arange(0, (width+1)*4, 1), minor=True)
    ax1.set_axisbelow(False)
    ax1.xaxis.grid(True, 'minor', linestyle='--', zorder=1)
    ax1.xaxis.grid(True, 'major', color='r', zorder=6)
    ax1.plot(np.arange(0, (width+1)*4, 1), data.flatten(), drawstyle='steps-post')
    ax1.set_ylim(-1.1,1.1)
    ax1.set_xlim(0,width*4)
    return ax1


fig = plt.figure(tight_layout=True)
plotwave(fig, 711, NORMAL(data), 'data')
plotwave(fig, 712, NRZ(data), 'NRZ')
plotwave(fig, 713, NRZ2(data), 'NRZ2')
plotwave(fig, 714, RZ(data), 'RZ')
plotwave(fig, 715, RZ2(data), 'RZ2')
plotwave(fig, 716, AMI(data), 'AMI')
plotwave(fig, 717, MAN(data), 'MAN')
plt.show()

"""
graphdata(NORMAL(data[1:24]))
graphdata(NRZ(data[1:24]))
graphdata(NRZ2(data[1:24]))
graphdata(RZ(data[1:24]))
graphdata(RZ2(data[1:24]))
graphdata(AMI(data[1:24]))
graphdata(MAN(data[1:24]))
"""

#print(np.reshape([1,2,3,4], (-1, 1) ) * [2, 3])
