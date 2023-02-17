# 2) Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100 шариков средний диаметр
# оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.
import numpy as np
alfa = 1.65
D = 4
sigma = np.sqrt(D)
Xgen = 17
Xv = 17.5
n = 100
Z = (Xv - Xgen)/(sigma/np.sqrt(n))
if Z > alfa:
    print('Гипотеза H0 не верна')
else:
    print('Гипотеза H0 верна')    