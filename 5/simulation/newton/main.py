x = 2.0

def f(x):
    return x**2.0 - 2.0

def fd(x):
    return 2.0*x

while abs(f(x)) > 10**-15:
    print(f"x = {x}, y = {f(x)}")
    x = x - f(x)/fd(x)
