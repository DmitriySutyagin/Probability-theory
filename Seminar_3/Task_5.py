# Устройство состоит из трех деталей. 
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2,
#  для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали 
# б). только две детали 
# в). хотя бы одна деталь 
# г). от одной до двух деталей?
from scipy.stats import binom
b1 = 0.1
b2 = 0.2
b3 = 0.25
PA = b1 * b2 * b3
l = binom.pmf(k=2, n=3, p=PA)
d = sum([b1 * (1-b1),b2 * (1-b2), b3 * (1-b3)])
binom.pmf(k=2, n=3, p=PA)
c = binom.pmf(k=1, n=3, p=PA) + binom.pmf(k=2, n=3, p=PA)
 
 




print(f'Вероятность того, что в первый месяц выйдут из строя хотя бы одна деталь = {round(d*100, 2)}%')
print(f'Вероятность того, что в первый месяц выйдут из строя все детали = {round(PA*100, 2)}%')
print(f'Вероятность того, что в первый месяц выйдут из строя только две детали = {round(l*100, 2)}%')
print(f'Вероятность того, что в первый месяц выйдут из строя только от одной до двух деталей = {round(c*100, 2)}%')





