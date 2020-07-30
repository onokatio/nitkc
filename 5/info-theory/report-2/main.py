#!/usr/bin/python

import numpy as np

prob = [
['A', 0.0642],
['B', 0.0127],
['C', 0.0218],
['D', 0.0317],
['E', 0.1031],
['F', 0.0208],
['G', 0.0152],
['H', 0.0467],
['I', 0.0575],
['J', 0.0008],
['K', 0.0049],
['L', 0.0321],
['M', 0.0198],
['N', 0.0574],
['O', 0.0632],
['P', 0.0152],
['Q', 0.0008],
['R', 0.0484],
['S', 0.0514],
['SP', 0.1859],
['T', 0.0796],
['U', 0.0228],
['V', 0.0083],
['W', 0.0175],
['X', 0.0013],
['Y', 0.0164],
['Z', 0.0005],
]

prob.sort(key=lambda x: x[1], reverse=True)
print(prob)

sign = []

sign.append('0')

for i in range(1,len(prob)):
    sign.append('1' + sign[i-1])

sumlen = 0
for i in range(len(prob)):
    print(f"{prob[i][0]} : {sign[i]}")
    sumlen += len(sign[i])*prob[i][1]

print(sumlen)
