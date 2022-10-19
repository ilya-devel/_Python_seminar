# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from random import random, randint

d = float(input("Укажите точность числа для вывода: "))
value = random() * randint(1, 20)
print(f"Оригинальное число = {value}")
count = 0
while d < 1:
    d *= 10
    count += 1
print(f"Число с указанной точностью = {round(value, count)}")

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

nvalue = int(input("Enter N values: "))
nums = set()
d = 2
while nvalue != 1:
    if nvalue % d == 0:
        nums.add(d)
        nvalue //= d
    else:
        d += 1
print(f"Simple multiples = {', '.join(list(map(str, nums)))}")

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

orig_num = str(randint(100000, 999999999999999999999999999999999999))
uniq_num = set()
print(f"Original num = {orig_num}")
for n in set(orig_num):
    if orig_num.count(n) == 1:
        uniq_num.add(n)

print(f"Uniq values = {(', '.join(uniq_num)) if (len(uniq_num) > 0) else 'None'}")


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def write_fumction(filename='homeworks4.txt'):
    from random import randint
    from os import sep as s

    k = randint(0, 5)
    tsk = list()
    for i in range(k):
        tsk.insert(0, f"({randint(-100, 100)} * x ** {i})")
    # print(f"{' + '.join(tsk)} = 0")
    with open(f'homeworks{s}{filename}', 'w', encoding='UTF-8') as wfile:
        wfile.write(f"{' + '.join(tsk)} = 0")


write_fumction()

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from os import sep as s

write_fumction('homeworks4_1.txt')
write_fumction('homeworks4_2.txt')
files = ['homeworks4_1.txt', 'homeworks4_2.txt']

funct = []

for file in files:
    with open(f'homeworks{s}{file}', 'r', encoding='UTF-8') as f:
        tmp = {m[1:-1].split(' * ')[1]: m[1:-1].split(' * ')[0] for m in
               f.read().strip().split('=')[0].strip().split(' + ')}
        funct.append(tmp)

ans = dict()
for key in set(funct[0].keys()).union(funct[1].keys()):
    ans[key] = (int(funct[0][key]) if key in funct[0].keys() else 0) + (
        int(funct[1][key]) if key in funct[1].keys() else 0)
with open(f'homeworks{s}homeworks4_3.txt', 'w', encoding='UTF-8') as file:
    file.write(' + '.join([f"({str(ans[k])} * {k})" for k in sorted(ans.keys(), reverse=True)]) + " = 0")
