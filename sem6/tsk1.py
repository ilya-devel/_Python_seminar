# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. Приоритет операций стандартный

def add(a, b):
    return a + b


def diff(a, b):
    return a - b


def mult(a, b):
    return a * b


def delim(a, b):
    return a / b


def app(txt):
    sign = ''
    for s in '+-*/':
        if s in txt:
            sign = s
            break
    if sign == '':
        return int(txt)
    else:
        a, b = txt.split(sign)
        if sign == '*': return mult(app(a), app(b))
        elif sign == '/': return delim(app(a), app(b))
        elif sign == '+': return add(app(a), app(b))
        elif sign == '-': return diff(app(a), app(b))


print(app('7+4*2/3'))
