# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры: - 1, 4, 8, 7, 5 -> 8 - 78, 55, 36, 90, 2 -> 90


values = []
for _ in range(5):
    values.append(int(input("Введите число: ")))

print(f"Максимальное значение из введённых: {max(values)}")