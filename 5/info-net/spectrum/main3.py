import numpy as np
import matplotlib.pyplot as plt

ar = np.random.randint(0,255,10000)
ar = np.random.normal(255,size=10000)
PN = np.random.randint(0,255,10000)
new_ar = ar * PN
arf = np.fft.fft(new_ar)
revert = np.fft.ifft(arf)
PN_new_ar = revert / PN

#plt.plot(ar)
plt.plot(PN_new_ar)
plt.show()
