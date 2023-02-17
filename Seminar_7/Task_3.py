# 2 ) Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть ли статистически значимые различия?
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150, 130, 135
import numpy as np
from scipy import stats
alfa = 0.05
x = np.array([150, 160, 165, 145, 155])
x_10 = np.array([140, 155, 150, 130, 135])
a = stats.wilcoxon(x, x_10)
print(a)
print('После проведения теста было выялено.Прием препарата в интервале в 10 минут не влияет на уровень давления пациентов.Потому что P-value > alfa')
