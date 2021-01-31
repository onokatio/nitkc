import numpy as np
import math

def f1(x):
    return 4 * x**3 - 10 * x**2 + 4*x + 5

def f2(x):
    return (1 / math.sqrt(2*math.pi)) * math.exp(-(x**2)/2)

l = 0
oldl = 0
s1 = 0;
s2 = 0;

width = 0.1

a=0
b=2
s1 = (b-a)/6 * ( f1(a) + 4*f1( (a+b)/2 ) + f1(b) )

a=-5
b=5
s1 = (b-a)/6 * ( f2(a) + 4*f2( (a+b)/2 ) + f2(b) )


print(s1)
print(s2)
