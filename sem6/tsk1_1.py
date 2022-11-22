# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. Приоритет операций стандартный
def add(lst):
    return sum(lst)


def diff(lst):
    res = lst[0]
    for i in lst[1:]:
        res -= i
    return res


def mult(lst):
    res = lst[0]
    for i in lst[1:]:
        res *= i
    return res


def delim(lst):
    res = lst[0]
    for i in lst[1:]:
        res /= i
    return res

def check_negativ(txt):
    find = False
    if txt.startswith('-'):
        for i in range(1, len(txt)):
            if not txt[i].isdigit():
                txt = f'(0{txt[:i]}){txt[i:]}'
                find = True
                break
    else:
        for i in range(0, len(txt)-1):
            if txt[i] in ('+-*/') and txt[i+1] == '-':
                for y in range(i+1, len(txt)-1):
                    if not txt[y].isdigit():
                        txt = f'{txt[:i+1]}(0{txt[i+1:y+2]}){txt[y+2:]}'
                        find = True
                        break
                if find:
                    break
    if find:
        return check_negativ(txt)
    else:
        return txt

def app(txt):
    if '(' in txt:
        start = 0
        for i in range(len(txt)):
            if txt[i] == '(':
                start = i
        fin = start + txt[start:].index(')')
        tmp = txt[start+1:fin]
        result = app(tmp)
        return app(f'{txt[:start]}{result}{txt[fin+1:]}')
    sign = ''
    for s in '+-*/':
        if s in txt:
            sign = s
            break
    if sign == '':
        if txt == '':
            return 0
        else:
            return int(txt)
    else:
        lst = list(map(app,txt.split(sign)))
        if sign == '*': return mult(lst)
        elif sign == '/': return delim(lst)
        elif sign == '+': return add(lst)
        elif sign == '-': return diff(lst)

def run_app(txt):
    txt = check_negativ(txt)
    print(txt)
    return app(txt)


# print(run_app('(-11+(-7))*4-4/(2+3)'))
# print(run_app('11/7/3'))
# print(run_app('-11/7/3'))
# print(run_app('7*-1'))
print(run_app('-11+7*4-4/-2+3*10'))
print(run_app('-7*-1'))
