# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число

from os import sep as s

with open(f'tsk1.txt', 'r', encoding='UTF-8') as f:
    lst_val = list(map(int, f.read().split('\n')))
if len(lst_val) > 1:
    for ind in range(1, len(lst_val)):
        if lst_val[ind] != lst_val[ind - 1] + 1:
            print(lst_val[ind - 1] + 1)
