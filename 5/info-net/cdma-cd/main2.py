import random
import numpy as np
import matplotlib.pyplot as plt
N=51200
x=np.arange(0, N)
y=np.zeros(N)
for i in range(N):
    y[i]+=random.uniform(-2,0)
    y[i]+=random.uniform(-2,0)

print(sum(y)/N)

plt.plot(x,y)
plt.show()
