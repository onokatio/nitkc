import numpy as np

r = np.random.randint(0,2,100)
print(r)

def manc(i):
    if i == 1:
        return [0,1]
    else:
        return [1,0]


result = []
for i in r:
    result.append(manc(i))

print(result)
