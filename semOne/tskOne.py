# Напишите программу, которая принимает на вход 2 числа и проверяет, является ли одно число квадратом другого

one = int(input("Enter first values: "))
two = int(input("Enter second values: "))

if one**2 == two:
    print("Второе число квадрат первого")
elif two**2 == one:
    print("Первое число квадрат второго")
else:
    print("Ни одно число не является квадратом второго")