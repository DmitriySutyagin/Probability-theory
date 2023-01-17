# В лотерее 100 билетов. Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
from math import factorial
import numpy as np


def C ( n, k):
    return np.math.factorial(n) //( np.math.factorial(k) * np.math.factorial(n - k))
m = C (2, 2)
n = C (100, 2)
Pa = m / n
print(f'Вероятность того, что 2 приобретенных билета окажутся выигрышными = {(round (Pa*100, 2))}%')