# Из колоды в 52 карты извлекаются случайным образом 4 карты.
#  a) Найти вероятность того, что все карты – крести.
#  б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
from math import factorial
import numpy as np


def C ( n, k):
    return np.math.factorial(n) //( np.math.factorial(k) * np.math.factorial(n - k))
m = C(13, 4)
n = C(52, 4)
Pa = m / n
print(f'Вероятность того что все карты крести = {round(Pa, 4)}')
l = sum([C(4,1), C(4,2),C(4,3), C(4,4)])
Pa = l / n
print(f'Вероятность того, что среди карт окажется один туз = {round(Pa, 4)}')
