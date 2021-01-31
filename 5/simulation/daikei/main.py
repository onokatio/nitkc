import numpy as np
import math

def f1(x):
    return 4 * x**3 - 10 * x**2 + 4*x + 5

def f2(x):
    return 1 / math.sqrt(2*math.pi) * math.exp(-(x**2)/2)

l = 0
oldl = 0
s1 = 0;
s2 = 0;

width = 0.1

for i in np.arange(0,3,width):
    oldl = l
    l = f1(i)
    s1+= (l + oldl)*width / 2
    #print(f"( {i}, {f1(i)} )")

l = 0
oldl = 0

for i in np.arange(-5,6,width):
    oldl = l
    l = f2(i)
    s2+= (l + oldl)*width / 2

print(s1)
print(s2)
