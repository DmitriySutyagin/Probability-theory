# В первом ящике находится 10 мячей, из которых 7 - белые. 
# Во втором ящике - 11 мячей, из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча. 
# Какова вероятность того, что все мячи белые? Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?
from math import factorial
import numpy as np
def C ( n, k):
    return np.math.factorial(n) //( np.math.factorial(k) * np.math.factorial(n - k))
m = C(16, 4)
n = C(21, 4)
Pa = m / n
print(f'Вероятность того, что все мячи белые = {round(Pa*100, 2)}%')
m = C(16, 2)
n = C(21, 4)
Pa = m / n
print(f'Вероятность того, что ровно два мяча белые = {round(Pa*100, 2)}%')
l = sum([C(4,1)*C(17, 3), C(4,2)*C(17, 2),C(4,3)*C(17,1), 1])
Pa = l / n
print(f'Вероятность того, что хотя бы один мяч белый = {round(Pa*100, 2)}%')
