# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

way_file = 'task_4_home.txt'
op = open(way_file, 'r')

li = []
for i in op:
    li.append(i)
op.close()
print(li)

li = li[0].split(' ')

li_num = []
for i in li:
    li_num.append(int(i))

count = 1
lost_number = None
for i in li_num:
    if i != count:
        lost_number = count
        break
    count += 1

print(f'Потерянное число: {lost_number}')
