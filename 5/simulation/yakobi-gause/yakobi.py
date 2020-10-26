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

x=1
y=1
z=1

# valtype 0=x 1=y 2=z
for i in range(100):
    tmpx = x
    tmpy = y
    tmpz = z
    x = (10 - tmpy - 2*tmpz)/7
    y = (8 - tmpx - 3 * tmpz)/8
    z = (6 - 2 * tmpx - 3 * tmpy)/9
    if abs(tmpx - x) < 10**-6 and abs(tmpy - y) < 10**-6 and abs(tmpz - z) < 10**-6 :
        break
    print(f"{x} {y} {z}")
