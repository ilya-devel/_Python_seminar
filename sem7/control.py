from operation import show_log, get_data
from os import system

def app():
    while True:
        system('clear')
        print("""
        1. Show logs
        2. Calculate
        """)

        ans = input()
        if ans == '1':
            show_log()
        elif ans == '2':
            get_data()
        else:
            print()
        ans = input('Try again? Y/n:')
        if ans.lower() != 'y':
            break