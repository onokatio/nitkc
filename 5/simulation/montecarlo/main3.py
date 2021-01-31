pi = 0

for i in range(1,100):
    n = 1/(i*2 -1) * (-1) ** (i+1)
    print(n)
    pi += n

pi *= 4

print(pi)
