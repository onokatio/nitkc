import numpy as np
import matplotlib.pyplot as plt

ar = np.random.randint(0,255,10000)
arf = np.fft.fft(ar)
print(ar)
print(arf)

plt.plot(ar)
plt.plot(arf)
plt.show()
