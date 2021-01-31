import numpy as np
import random
import math

def f1(x):
    return 4 * x**3 - 10 * x**2 + 4*x + 5

def f2(x):
    return 1 / math.sqrt(2*math.pi) * math.e ** (x**2 / -2)

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

rangex = 2
rangey = 5

for i in range(1000):
    x = random.randrange(0*scale,rangex*scale)/scale
    y = random.randrange(0*scale,rangey*scale)/scale
    if check(x,y,f1):
        n+=1
    else:
        m+=1

s1 = rangex * rangey * (n / n+m)


rangex = -5
rangey = 5

for i in range(1000):
    x = random.randrange(rangex*scale,0)/scale
    y = random.randrange(0*scale,rangey*scale)/scale
    if check(x,y,f2):
        n+=1
    else:
        m+=1

s2 = rangex * rangey * (n / n+m)

print(f"{s1}")
print(f"{s2}")
