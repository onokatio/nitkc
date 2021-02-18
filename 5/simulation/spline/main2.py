import numpy as np
import math
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [9,4,6,3]

A = []
b = []

for line_num in range(len(x)-1):
    for st_en in range(2):
        row = []
        for hoge in range(line_num):
            row += [0 for i in range(len(x))]
        for num in range(len(x)):
            num = len(x)-1 - num
            row.append(x[line_num+st_en] ** num)
        """
        row += [
            x[line_num+st_en] ** 3,
            x[line_num+st_en] ** 2,
            x[line_num+st_en] ** 1,
            x[line_num+st_en] ** 0,
        ]
        """
        for hoge in range(len(x)-2 - line_num):
            row += [0 for i in range(len(x))]
        b.append(y[line_num+st_en])
        print(row)
        A.append(row)

for line_num in range(1,len(x)-1):
    for two_or_three in range(2):
        row = []
        for hoge in range(line_num-1):
            row += [0 for i in range(len(x))]
        if two_or_three == 0:
            for st_en in range(2):
                for num in range(len(x)-1):
                    num = len(x)-2 - num
                    row.append( (x[line_num] ** num) * (num+1) * (-1) ** st_en)
                row.append(0)
                """
                row += [
                    (x[line_num] ** 2) * 3 * (-1) ** st_en,
                    (x[line_num] ** 1) * 2 * (-1) ** st_en,
                    (x[line_num] ** 0) * 1 * (-1) ** st_en,
                    0,
                ]
                """
        else:
            for st_en in range(2):
                for num in range(len(x)-2):
                    num2 = len(x)-1 - num
                    num3 = num2-2
                    row.append(x[line_num] ** num3 * math.factorial(num2) * (-1) ** st_en)
                row.append(0)
                row.append(0)
                """
                row += [
                    x[line_num] * 6 * (-1) ** st_en,
                    2 * (-1) ** st_en,
                    0,
                    0,
                ]
                """
        for hoge in range(len(x)-2 - line_num):
            row += [0 for i in range(len(x))]
        A.append(row)
        print(row)

for line_num in range(2):
    if line_num == 1:
        line_num = len(x)-1
    row = []
    for hoge in range(line_num-1):
        row += [0 for i in range(len(x))]
    """
    for num in range(len(x)-2):
        num2 = len(x)-1 - num
        num3 = num2-2
        row.append(x[line_num] ** num3 * math.factorial(num2))
    row.append(0)
    row.append(0)
    """

    """
    row += [
        x[line_num] * 6,
        2,
        0,
        0,
    ]
    """
    row += [
        x[line_num] ** 2 * 3,
        x[line_num] * 2,
        1,
        0,
    ]
    for hoge in range(len(x)-2 - line_num):
        row += [0 for i in range(len(x))]
    print(row)
    A.append(row)


for i in range(12-len(b)):
    b.append(0)

print(b)

print(A)
A = np.matrix(A)
print(A)

result = np.linalg.solve(A,b)

print(result)

params = []
params.append([result[0],result[1],result[2],result[3]])
params.append([result[4],result[5],result[6],result[7]])
params.append([result[8],result[9],result[10],result[11]])

print(params)

def f(x,p):
    return p[0] * x ** 3 + p[1] * x ** 2 + p[2] * x ** 1 + p[3] * x ** 0

for i in range(len(x)-1):
    xrange = np.arange(x[i],x[i+1]+0.1,0.1)
    yrange = f(xrange,params[i])
    plt.plot(xrange,yrange)


for i in range(len(x)):
    plt.plot(x[i],y[i],marker='.')

plt.show()
