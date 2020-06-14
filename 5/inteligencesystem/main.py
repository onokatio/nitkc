#!/usr/bin/python

def f(a):
    return pow(a-1.0,2)*pow(a+1.0,2)

def fd(a):
    return 4*a*(a-1.0)*(a+1.0)

a0 = 2.0
n = 0.01

a = a0
while f(a) > pow(10, -10):
    print("a = ", a)
    print("f(a)  =", f(a))
    nexta = a - n*fd(a)
    print("nexta = ", nexta)
    a = nexta
