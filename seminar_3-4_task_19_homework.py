# Составить список простых множителей натурального числа N.

num = int(input('Введите число: '))
# num = 144
list_1 = []
i = 2

# while num % i != 0:
#     i += 1

while num != 1:

    if num % i == 0:
        num /= i
        list_1.append(i)
    else:
        i += 1

print(list_1)
