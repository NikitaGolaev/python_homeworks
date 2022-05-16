# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
# k = int(input('Коэффициет k: '))
k = 10

li = [random.randint(0, 11) for i in range(k + 1)]
print(li)

res = [f'{li[i]}*x^{len(li) - i - 1}' if len(li) - i - 1 != 0 else f'{li[i]}' for i in range(len(li)) if li[i] != 0]
print(' + '.join(res) + ' = 0')

f = open('task_2.txt', 'a')
f.write(' + '.join(res) + ' = 0\n')
f.close()
