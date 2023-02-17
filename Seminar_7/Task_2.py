# 2 ) Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть ли статистически значимые различия?
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150, 130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125
import numpy as np
from scipy import stats
alfa = 0.05
x = ([150, 160, 165, 145, 155])
x_10 = ([140, 155, 150, 130, 135])
x_30 = ([130, 130, 120, 130, 125])
a = stats. friedmanchisquare(x, x_10, x_30)
print(a)
print('После проведения теста было выялено.Прием препарата в интервале в 30 минут влияет на уровень давления пациентов.Потому что P-value < alfa')