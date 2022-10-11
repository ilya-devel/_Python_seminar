# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. *Пример:* - Для N = 5: 1, -3, 9, -27, 81

value = int(input("Enter N values: "))
# mult = 1
# for i in range(value):
#     print(3 ** i * mult)
#     mult *= -1

print(", ".join([str(3 ** i * (1 if i % 2 == 0 else -1)) for i in range(value)]))
