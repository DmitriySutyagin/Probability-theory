# 2)Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
import numpy as np
from scipy import stats
x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
t = stats.t.ppf(0.975, len(x) - 1)
SE = np.sqrt((np.var(x, ddof=1)) / len(x))
L = np.mean(x) - t * SE
R = np.mean(x) + t * SE
print(f'Доверительный интервал от {L} до {R}')