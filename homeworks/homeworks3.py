# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

from random import randint

lst = [randint(1, 10) for _ in range(randint(10, 21))]
print(f"Список: {', '.join([str(x) for x in lst])}")
print(f"Суммна нечетных элементов в списке: {sum(lst[1::2])}\n")

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

lst = [randint(1, 10) for _ in range(randint(10, 21))]
print(f"Список: {', '.join([str(x) for x in lst])}")
print(
    f"Произведение пар чисел списка => {', '.join([str(lst[i] * lst[-1 - i]) for i in range(len(lst) // 2 + len(lst) % 2)])}\n")

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

from random import random


def create_lst_and_find_min_max():
    tmp_lst = [round(random() * randint(10, 21), 2)]
    my_min = tmp_lst[0] % 1
    my_max = tmp_lst[0] % 1
    for _ in range(randint(5, 11)):
        tmp_lst.append(round(random() * randint(10, 21), 2))
        if my_min > tmp_lst[-1] % 1:
            my_min = tmp_lst[-1] % 1
        elif my_max < tmp_lst[-1] % 1:
            my_max = tmp_lst[-1] % 1
    return tmp_lst, my_min, my_max


lst = create_lst_and_find_min_max()
print(f"Список: {', '.join([str(x) for x in lst[0]])}")
print(f"Разница между максимальным и минимальным значением дробной части равно: {round(lst[2] - lst[1], 2)}\n")

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Simple

value = int(input("Enter value: "))
print(f"Число {value} в двоичном виде, равно {str(bin(value))[2:]}")


# Hard

def int_to_bin(num: int):
    if num <= 0:
        return ''
    else:
        return str(num % 2) + int_to_bin(num // 2)


print(f"Число {value} в двоичном виде, равно {int_to_bin(value)}\n")

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

value = int(input("Укажите количество необходимых чисел Фибоначи в обоих направлениях (негативные и позитивные): "))
lst_fib = [1, 0, 1]
for _ in range(value - 1):
    lst_fib.insert(0, lst_fib[1] - lst_fib[0])
    lst_fib.append(lst_fib[-2] + lst_fib[-1])
print(f"Список чисел Фибоначчи: {', '.join([str(x) for x in lst_fib])}")


# Сгруппировать слова по общим группам

simple_input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
my_out = dict()
for i in simple_input:
    tmp = ''.join(sorted(i))
    if tmp in my_out:
        my_out[tmp].append(i)
    else:
        my_out[tmp] = [i]
print(f"Слова сгруппированы по типу <ключ - список>:\n"
      f" {', '.join([f'{k}: {v}'for k, v in my_out.items()])}")