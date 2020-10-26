import numpy as np

"""
[7,1,2,10]
[1,8,3,8]
[2,3,9,6]
"""

a1 = [7,1,2,10]
a2 = [1,8,3,8]
a3 = [2,3,9,6]


matrix = np.matrix(
[[7,1,2,10],
[1,8,3,8],
[2,3,9,6]])

x=0
y=0
z=0

# valtype 0=x 1=y 2=z
for i in range(100):
    tmpx = x
    tmpy = y
    tmpz = z
    x = (10 - y - 2*z)/7
    y = (8 - x - 3 * z)/8
    z = (6 - 2 * x - 3 * y)/9
    if abs(tmpx - x) < 10**-7 and abs(tmpy - y) < 10**-7 and abs(tmpz - z) < 10**-7 :
        break
    print(f"{x} {y} {z}")
