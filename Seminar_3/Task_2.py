# В первом ящике находится 8 мячей, из которых 5 - белые.
#  Во втором ящике - 12 мячей, из которых 5 белых. 
#  Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяерча белые?
from math import factorial
import numpy as np
from scipy.stats import binom
def C ( n, k):
    return np.math.factorial(n) //( np.math.factorial(k) * np.math.factorial(n - k))
m = C(5, 2)
n = C(8, 2)
P1 = round(m / n, 3)
m2 = C(5, 4)
n2 = C(12, 4)
P2 = round(m2 / n2, 3)
p = round(P1 * P2, 3)
a = 6
b = 3
q = 1 - p

Pz = round(C(a, b) * p**(b) * q**(a - b), 7)

print(f'Вероятность того, что 3 мяерча белые = {Pz}')
