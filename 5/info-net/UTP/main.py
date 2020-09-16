import numpy as np

Hz0 = np.array([1,4,10,20,25,31.25,62.5,100])
Hz = np.array(Hz0)

db = 1.967 * np.sqrt(Hz) + 0.023 * Hz + 0.05 * np.sqrt(Hz)
Next = 35.3 - 15 * np.log10(Hz/100)
Fext = 23.8 - 20 * np.log10(Hz/100)

print(Hz)
print(db)
print(Next)
print(Fext)
