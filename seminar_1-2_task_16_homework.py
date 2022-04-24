# Написать программу проверки, является ли строка палиндромом

str = 'texet'

# if str

average = (len(str) + 1) // 2
# print((len(str) + 1) // 2)

i = 0
while i <= average:
    if str[i] == str[len(str) - (i + 1)]:
        print('Проверка прошла')
        i += 1
    else:
        print('Не палидром')
        break


exit()
i = 1
while i <= len(str):
    print(str[len(str) - i], end=' ')
    # print(len(str))
    i += 1
