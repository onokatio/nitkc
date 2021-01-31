import numpy as np
import random
import math

def myrand(x):
    return (11 * x + 57) % 6000

def f1(x):
    return math.sqrt(1 - x**2)

# return True when Point is in the figure,
def check(x, y, f):
    if f(x) <= y:
        return True
    else:
        return False

s1 = 0

scale = 1000
n = 0
m = 0
seed = 8

rangex = 1
rangey = 1

for i in range(1000):
    seed = myrand(seed)
    x = ( seed % (rangex*scale) ) / scale
    seed = myrand(seed)
    y = ( seed % (rangey*scale) ) / scale
    if check(x,y,f1):
        n+=1
    else:
        m+=1

s1 = rangex * rangey * (n / n+m)

print(f"{4*(n/m)}")
