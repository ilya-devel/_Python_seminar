# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

value = float(input("Enter value: "))

# Simple

print(sum([int(x) for x in str(value) if x.isdecimal()]))

sum_val = 0
for i in str(value):
    if i.isdecimal():
        sum_val += int(i)
print(sum_val)

# Hard

sum_val = 0
while value % 1 != 0:
    value *= 10
value = int(value)
while value > 0:
    sum_val += value % 10
    value = value // 10

print(sum_val)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

value = int(input("Enter value: "))

lst = []
text = []
for i in range(1, value + 1):
    if lst == []:
        lst.append(i)
    else:
        lst.append(lst[-1] * i)
    text.append('*'.join([str(x) for x in range(1, i + 1)]))
print(lst)
print(f"({', '.join(text)})")

# Задайте список из N чисел последовательности (1+1/N)^N и выведите на экран их сумму

value = int(input("Enter value: "))
print(f"{sum([((1 + 1 / x) ** x) for x in range(1, value + 1)]):.2f}")

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

from random import randint
from os import sep as s

value = int(input("Enter value: "))
lst = [randint(-value, value + 1) for _ in range(randint(10, 21))]
print(lst)
with open(f'homeworks{s}file.txt', 'r') as file:
    print(sum([lst[x] for x in list(map(int, file.read().split('\n')))]))

# Реализуйте алгоритм перемешивания списка.

from random import randint

lst = [randint(1, 100) for _ in range(randint(10, 21))]
print(lst)
for i in range(len(lst)):
    ind = randint(0, len(lst) - 1)
    lst[i], lst[ind] = lst[ind], lst[i]
print(lst)

# ДОП. задача на алгоритмы с реальных собеседований Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

from random import randint

lst1 = [randint(1, 100) for _ in range(randint(10, 21))]
lst2 = [randint(1, 100) for _ in range(randint(10, 21))]

general = []
for i in range(len(lst1)):
    for y in range(len(lst2)):
        if lst1[i] == lst2[y] and y not in general:
            general.append(y)
            break
print([lst2[x] for x in general])
