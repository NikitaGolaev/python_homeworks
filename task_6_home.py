# Напишите программу, удаляющую из текста все слова содержащие "абв".

text = 'Реку́рсия — определение, описание, изображение какого-либо объекта или процесса внутри самого \
этого объекта или процесса, то есть ситуация, когда объект является частью самого себя.'

text_list = text.split()


def f_clear(li, x):
    list_main = []
    for i in range(len(li)):
        for k in li[i]:
            if x not in li[i]:
                list_main.append(li[i])
            break
    return list_main


print(text_list := f_clear(text_list, 'а'))
print(text_list := f_clear(text_list, 'б'))
print(text_list := f_clear(text_list, 'в'))

text_new = ''
for i in text_list:
    text_new += i
    text_new += ' '
print(text_new)
