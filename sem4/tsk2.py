# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

a, b, c = list(map(int, input("Введите значения A B C для формулы Ax² + Bx + C через пробел: ").split()))

d = b ** 2 - (4 * a * c)
if d < 0:
    print("Решений нет")
elif d == 0:
    print(-b / (2 * a))
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f"X1 = {x1}; X2 = {x2}")

from sympy import Symbol, solve

x = Symbol('x')
print(solve(a * x ** 2 + b * x + c, x))
