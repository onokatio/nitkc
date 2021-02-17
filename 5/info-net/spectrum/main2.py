import numpy as np
import matplotlib.pyplot as plt

ar = np.random.randint(0,255,10000)
ar = np.random.normal(255,size=10000)
PN = np.random.randint(0,255,10000)
new_ar = ar * PN
arf = np.fft.fft(ar)
new_arf = np.fft.fft(new_ar)

#plt.plot(ar)
plt.plot(new_arf)
plt.show()
