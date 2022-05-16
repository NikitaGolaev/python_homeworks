# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел.


list_1 = [1, 4, 3, 7, 15, 17]
# list_1 = set(list_1)

list_2 = set()
print(type(list_2))


# list_2.add(3)
# print(list_2)

i = 0
while len(list_1) != 0:
    list_2.add(list_1[i])
    list_1.pop(i)

# for i in range(0, len(list_1)):
#     # var = list_1[i]
#     print(list_1[i], end=' ')
#     list_2.add(list_1[i])
#     # list_2.add(var)
print()
print(list_2)
