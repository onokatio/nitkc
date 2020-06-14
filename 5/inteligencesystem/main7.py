#!/usr/bin/python

import math

def f(x,y):
    return math.sin(x)+2*x*math.cos(y)+0.2*x*x+0.2*y*y

def fdx(x,y):
    return math.cos(x)+math.cos(y)+0.4*x

def fdy(x,y):
    return 2*x+0.4*y

x = 3.0
y = 3.0
n = 0.01

for i in range(10000):
    print("x = ", x)
    print("y = ", y)
    print("f(x,y)  =", f(x,y))
    nextx = x - n*fdx(x,y)
    nexty = y - n*fdy(x,y)
    #print("nextx = ", nextx)
    #print("nexty = ", nexty)
    x = nextx
    y = nexty
