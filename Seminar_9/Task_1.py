# 1) Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак),
# а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
 
n = (len(x) + len(y)) / 2

b1 = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/ (n*np.sum(x**2) - np.sum(x)**2)
b0 =  np.mean(y) - b1 * np.mean(x)
y_pred = b0 + b1 * x

model = LinearRegression()
x = x.reshape(len(x), 1)
regres = model.fit(x, y)
print(f'Коэффицент корреляции равен {regres.coef_}')
print(f'Предиктовое значение y равно {y_pred}')
print(f'Значение b1 равно {b1}')
print(f'Значение b0 равно {b0}')
print(f'Значение интерсепта равно {regres.intercept_}')
