# Найти НОК двух чисел.

a = int(input('Введите число \'a\': '))
b = int(input('Введите число \'b\': '))


def fun_num_nok(x1, x2):
    i = 1
    num_nok = x1
    while num_nok % x2 != 0:
        num_nok = x1 * i
        i += 1
    return num_nok


if a > b:
    print(fun_num_nok(a, b))
else:
    print(fun_num_nok(b, a))
