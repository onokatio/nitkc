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

width = 50

data = data[0:width]

fig = plt.figure()
ax1 = fig.add_subplot(711)
ax1.plot(range(width * 4), NORMAL(data).flatten())
ax = fig.add_subplot(712).plot(range(width * 4), NRZ(data).flatten(), drawstyle='steps-pre')
ax = fig.add_subplot(713).plot(range(width * 4), NRZ2(data).flatten())
ax = fig.add_subplot(714).plot(range(width * 4), RZ(data).flatten())
ax = fig.add_subplot(715).plot(range(width * 4), RZ2(data).flatten())
ax = fig.add_subplot(716).plot(range(width * 4), AMI(data).flatten())
ax = fig.add_subplot(717).plot(range(width * 4), MAN(data).flatten())
ax1.grid(True, 'both', 'both')
plt.show()

graphdata(NORMAL(data[1:24]))
graphdata(NRZ(data[1:24]))
graphdata(NRZ2(data[1:24]))
graphdata(RZ(data[1:24]))
graphdata(RZ2(data[1:24]))
graphdata(AMI(data[1:24]))
graphdata(MAN(data[1:24]))

#print(np.reshape([1,2,3,4], (-1, 1) ) * [2, 3])
