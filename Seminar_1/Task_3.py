# В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?
from math import factorial
import numpy as np


def C ( n, k):
    return np.math.factorial(n) //( np.math.factorial(k) * np.math.factorial(n - k))
m = C (9, 3)
n = C (15, 3)
Pa = m / n
print(f'Вероятность того, что все извлеченные детали окрашены = {(round (Pa*100, 4))}%')