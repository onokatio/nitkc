#!/bin/python3
print("number:")
n = input()
print("a:")
a = input()
print("b:")
b = input()
print("count:")
count = input()

def f(x):
    return x*x-2

x1 = int(a)
x2 = int(b)
for i in range(int(count)):
    x = (x1+x2)/2
    y = f(x)
    print("f(%d) = %d", x, y)
    if(y < 0): # x is too low
        x1 = x
        x2 = x2
    if(y > 0): # x is too high
        x1 = x1
        x2 = x
