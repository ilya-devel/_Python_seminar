import math_operation
from datetime import datetime as dt
import os.path as check


def get_value(name):
    return int(input(f'Enter {name} values: '))


def get_operation():
    return input('Enter type operation (+,-,*,/):')


def write_log(a, oper, b, result):
    if not check.isfile('log.csv'):
        with open('log.csv', 'w') as log:
            log.write(f'Date;First Value;Operation;Second Value;Result\n')
    with open('log.csv', 'a') as log:
        log.write(f'{dt.strftime(dt.now(),"%Y-%m-%d %H:%M:%S")};{a};{oper};{b};{result}\n')

def show_log():
    with open('log.csv', 'r') as log:
        for row in log.readlines():
            print(''.join(list(map(lambda x: f'{x:^20}', row.split(';')))))


def get_data():
    a = get_value('first')
    oper = get_operation()
    b = get_value('second')
    result = calc(a, oper, b)
    write_log(a, oper, b, result)
    print(result)


def calc(a, oper, b):
    if oper == '+':
        return math_operation.add(a, b)
    elif oper == '-':
        return math_operation.diff(a, b)
    elif oper == '*':
        return math_operation.mult(a, b)
    elif oper == '/':
        return math_operation.delim(a, b)
    return 'Invalid data'
