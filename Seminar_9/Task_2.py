# 2)Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = (len(x) + len(y)) / 2
B1 = 0.025
def mse_(B1, y, x, n):
    return np.sum((B1*x-y)**2)/n
alfa = 1e-6
for i in range(12000):
    B1 -= alfa * (2/n) * np.sum((B1*x-y)*x)/n
    if i % 100 == 0:
        print(f'Iterator = {i}, B1 = {B1}, mse = {mse_(B1, y, x, n)}')
print('Делаем вывод: модель рабочая т.к. значени B1 перестали изменятся на 11300-ой интерации')
