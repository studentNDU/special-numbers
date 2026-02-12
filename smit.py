import matplotlib.pyplot as plt
import numpy as np
def factors(n):
    f, d = [], 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    return f + [n] if n > 1 else f
def s(n): return sum(int(d) for d in str(n))
N = 10000
x = np.arange(1, N + 1)
y_prime, y_smith = [], []
c_p, c_s = 0, 0
for n in x:
    f = factors(n)
    # Просте число має лише один множник у нашому списку (саме себе)
    if len(f) == 1: c_p += 1  
    # Число Сміта: складене (len>1) і суми цифр збігаються
    elif s(n) == sum(map(s, f)): c_s += 1
    y_prime.append(c_p)
    y_smith.append(c_s)
plt.plot(x, y_prime, label='Прості', color='blue')
plt.plot(x, y_smith, label='Сміта', color='orange')
plt.legend(); plt.grid(); plt.show()
