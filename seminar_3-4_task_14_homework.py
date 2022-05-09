# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т.е. для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

# k = int(input('Введите число фибоначчи: '))
k = 8


def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


list_fibo = []
for e in range(0, k + 1):
    list_fibo.append(fib(e))

# print(list_fibo)


def fib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return fib(n + 2) - fib(n + 1)


list_nfibo = []
for e in range(-k, 0):
    list_nfibo.append(fib(e))

# print(list_nfibo)

list_common = list_nfibo + list_fibo
print(list_common)
