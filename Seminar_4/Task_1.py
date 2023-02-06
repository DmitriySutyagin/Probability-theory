# 1)Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
list = []
for i in range(201, 801):
    list.append(i)
s = sum(list) / len(list)

for i in range(len(list)):
  list[i] -= s
a = sum(list)**2
print(f'Диссперсия равна {a / len(list)}')


print(f'Среднее значение равно {s}')
