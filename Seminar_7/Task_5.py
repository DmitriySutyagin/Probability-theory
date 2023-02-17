# 5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
#  Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. 
# Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
import numpy as np 
x = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
n = 10
Sgen = 2.5
alfa = 0.05
Z = (np.mean(x) - Sgen)/((np.std(x) / np.sqrt(n)))
print(Z)
print('После проведения теста.Принимаем утверждение что партия изготавливается со средним арифметическим 2.5 см.Потому что расчетное значение больше, чем alfa/2')