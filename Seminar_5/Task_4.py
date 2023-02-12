# Задачу 4 решать ,с помощью функции. Есть ли статистически значимые различия в росте дочерей и матерей?
# 4) Рост матерей 172 177, 158, 170, 178,175, 164, 160, 169
# Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160
import numpy as np
from scipy import stats
x = np.array([172, 177, 158, 170, 178,175, 164, 160, 169])
y = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])
a = np.mean(x)
b = np.mean(y)
alfa = 0.05
c = np.std(x, ddof= 1)
d = np.std(y, ddof= 1)
t = (a - b) / (c / len(x) + d / len(y))
# print(t)
t1 = stats.t.ppf(alfa, df = 2 * (len(x) - 1))
t2 = stats.t.ppf(1 - alfa, df = 2 * (len(y) - 1))
# print(t1, t2)
if t > t2 or t < t1:
    print('Нет статисчески значимых различий')
else:
    print('Есть статистически значимые различия')