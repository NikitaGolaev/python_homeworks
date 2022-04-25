# Написать программу проверки, является ли строка палиндромом

str = 'texet'
# str = 'tex1et'

average = (len(str) + 1) // 2
i = 0
bool_check = False

while i <= average:
    if str[i] == str[len(str) - (i + 1)]:
        i += 1
        bool_check = True
    else:
        bool_check = False
        break

if bool_check == True:
    print('Палидром')
else:
    print('Не палидром')
