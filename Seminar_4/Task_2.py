# 2)О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.
D = 0.2
L = 0.5
H = 12
S = D * H
R = L + S 
list = []
while L < R + 0.1:
    list.append(L)
    L += 0.1
a = sum(list) / len(list)
# print(round(S, 1))
print(f'Правая граница равна {round(R, 1)}')
# print(list)
print(f'Среднее значение = {round(a, 1)}')