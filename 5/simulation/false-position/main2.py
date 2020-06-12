#!/bin/python3
print("a:")
a = input()
print("b:")
b = input()
print("count:")
count = input()

def f(x):
    return x*x-2

a = int(a)
b = int(b)
for i in range(int(count)):
    w = (a*f(b) - b*f(a))/(f(b)-f(a))
    y = f(w)
    print("f(", w, ") = ", y)
    if(y < 0): # x is too low
        a = w
        b = b
    if(y > 0): # x is too high
        a = a
        b = w
