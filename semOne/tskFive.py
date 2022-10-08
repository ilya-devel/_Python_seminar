# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

val = int(input("Enter values: "))
if (val % 5 == 0 and val % 10 == 0 or val % 15 == 0) and val % 30 != 0:
    print("Correct!!!")
else:
    print("Uncorrect")