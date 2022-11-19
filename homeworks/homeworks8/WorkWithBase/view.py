import control

MENU = """
1. Показать список
2. Добавить в список
3. Найти в списке
"""


def app():
    while True:
        print(MENU)
        operation = input('Check operation: ')
        control.run_operation(operation)
        ans = input('\nTry Again? Y/n: ')
        if ans.lower() == 'n':
            break
