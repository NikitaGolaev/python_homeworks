# Вычислить число c заданной точностью d.
# Пример: при d = 0.001, Пи = 3.141. 10(-1) <= d <= 10(-10).

d = float(input('Задайте \'d\' в формате: d = 0.001, \nи в диапазоне: 10 ** (-10) <= d <= 10 ** (-1): \n'))
p = 3.1415926535


def reducing_the_number(arg1, arg2):

    x = int(arg2 / arg1)
    x = x * arg1
    return x


if d <= 10 ** (-1) and d >= 10 ** (-10):
    print(f'Число \'Пи\' с заданной точностью {d}: {reducing_the_number(d, p)}')
else:
    print('Вы ввели не верное число.')
