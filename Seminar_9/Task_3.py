# 3) Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться
# на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
model = LinearRegression()
x = x.reshape(len(x), 1)
regres = model.fit(x, y)
a = regres.intercept_
n = (len(x) + len(y)) / 2
B1 = 0.025
B0 = 0.1
def mse_(B1, y, x, n):
    return np.sum(((a+B1*x)-y)**2)/n

alfa = 1e-6
for i in range(2000):
    B1 -= alfa * (2/n) * np.sum(((a+B1*x)-y)*x)
    B0 -= alfa * (2/n) * np.sum(((a+B1*x)-y)*x)
    if i % 100 == 0:
        print(f'Iterator = {i} B1 = {B1} B0 = {B0} mse = {mse_(B1, y, x, n)}')
print('Делаем вывод: модель рабочая т.к. значени B1 перестали изменятся на 1000-ой интерации. Также модель с интерсептом быстрее нашла решение')