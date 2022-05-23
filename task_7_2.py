# Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека:
# a) Добавьте игру против бота;
# b) Подумайте как наделить бота "интеллектом".

from random import randint

start = 2022
print(f'Конфет на столе: {start}')
while start >= 0:
    if start > 28:
        rand = randint(1, 28)
        first_player = start - rand
        print(f'Первый игрок взял конфет: {rand} - Осталось конфет на столе: {first_player}')
        # print(f'Осталось конфет на столе: {first_player}')
        start -= rand
    else:
        start -= 28
        print('Первый игрок забирает последние конфеты, и выигрывает!')
        break

    if start > 28:
        rand = randint(1, 28)
        print(f'Второй игрок взял конфет: {rand} - Осталось конфет на столе: {first_player}')
        first_player = start - rand
        # print(f'Осталось конфет на столе: {first_player}')
        start -= rand
    else:
        start -= 28
        print('Второй игрок забирает последние конфеты, и выигрывает!')
