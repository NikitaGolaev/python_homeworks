# Реализовать алгоритм перемешивания списка.

from random import randint

list_1 = [1, 4, 73, 13, 99]
list_2 = []

for i in range(0, len(list_1)):
    random_number = randint(0, len(list_1) - 1)
    list_2.append(list_1[random_number])
    list_1.pop(random_number)

print(list_2)
