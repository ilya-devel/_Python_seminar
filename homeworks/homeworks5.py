# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('homeworks5_text.txt', 'r', encoding='UTF-8') as f:
    print(' '.join(list(filter(lambda x: 'абв' not in x.lower(), f.read().split()))))


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

class CandyGame:
    def __init__(self):
        self.candy = 100
        self.mode = 0
        self.turn = -1
        self.run()

    def run(self):
        while True:
            self.turn *= -1
            print(f"На столе осталось {self.candy} конфет")
            if self.turn > 0:
                print("Ход первого игрока, укажите сколько конфет возьмёте от 1 до 28")
            else:
                print("Ход второго игрока, укажите сколько конфет возьмёте от 1 до 28")
            val = input()
            while not self.check_input(val):
                val = input("Try again: ")
            self.candy -= int(val)
            if self.check_win():
                break
        print('Game End')

    def check_input(self, value):
        if value.isdigit() and 0 < int(value) < 29:
            return True
        else:
            print("Не верные данные")
            return False

    def check_win(self):
        if self.candy <= 0:
            print(f"Победил {'первый' if self.turn > 0 else 'второй'} игрок, он забирает все конфеты")
            return True
        elif self.candy < 29:
            print(f"Т.к. осталось {self.candy}")
            print(f"Победил {'первый' if self.turn < 0 else 'второй'} игрок, он забирает все конфеты")
            return True
        return False

CandyGame()

# Создайте программу для игры в ""Крестики-нолики"".

class XzeroGame:
    def __init__(self):
        self.lst = [['[1]', '[2]', '[3]'], ['[4]', '[5]', '[6]'], ['[7]', '[8]', '[9]']]
        self.turn = -1
        self.run()

    def check_win(self):
        tmp = self.lst
        for i in range(3):
            if (len(set(tmp[i])) == 1) or (len(set(list(map(lambda x: x[i], tmp)))) == 1):
                return True
            elif (len({tmp[0][0], tmp[1][1], tmp[2][2]}) == 1) or (len({tmp[0][2], tmp[1][1], tmp[2][0]}) == 1):
                return True
        return False

    def show(self):
        for i in self.lst:
            print(''.join(i))

    def run(self):
        while not self.check_win():
            self.show()
            self.turn *= -1
            if self.turn > 0:
                print("Ход первого игрока, укажите свободную позицию от 1 до 9")
            else:
                print("Ход второго игрока, укажите свободную позицию от 1 до 9")
            val = input()
            while not self.check_input(val):
                val = input("Try again: ")
            for i in range(len(self.lst)):
                for j in range(len(self.lst[i])):
                    if f'[{val}]' == self.lst[i][j]:
                        self.lst[i][j] = '[X]' if self.turn > 0 else '[O]'
                        break
        print(f"Поздравляем, выиграл {'Первый' if self.turn > 0 else 'Второй'} игрок")

    def check_input(self, value):
        if not value.isdigit() or 0 > int(value) > 9:
            print("Invalid value")
            return False
        for i in self.lst:
            if f'[{value}]' in i:
                return True
        return False


XzeroGame()


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def my_pack(txt=''):
    if txt == '':
        return ''
    out = ''
    ch = txt[0]
    count = 1
    for i in range(1, len(txt)):
        if txt[i] == ch:
            count += 1
            if i == len(txt) - 1:
                out += f'{count}{ch}'
        else:
            if i == len(txt) - 1:
                if count == 1:
                    ch += txt[i]
                    out += f'{-len(ch)}{ch}'
                else:
                    out += f'{count}{ch}1{txt[i]}'
            else:
                if txt[i] == txt[i + 1]:
                    if len(ch) > 1:
                        out += f'{-len(ch)}{ch}'
                    else:
                        out += f'{count}{ch}'
                    ch = txt[i]
                    count = 1
                else:
                    if count == 1:
                        ch += txt[i]
                    else:
                        out += f'{count}{ch}'
                        ch = txt[i]
                        count = 1

    return out


def my_unpack(txt=''):
    if txt == '':
        return ''
    out = ''
    ph = False
    ch = ''
    count = ''
    for i in range(len(txt)):
        if txt[i] == '-':
            if len(ch) > 0:
                if ph:
                    out += ch
                else:
                    out += f'{int(count) * ch}'
                ch = ''
                count = txt[i]
            ph = True

        else:
            if txt[i].isdigit():
                if len(ch) < 1:
                    count += txt[i]
                elif len(ch) > 0:
                    if ph:
                        out += ch
                    else:
                        out += f'{int(count) * ch}'
                    ch = ''
                    count = txt[i]
                    ph = False
            else:
                ch += txt[i]
        if i == len(txt) - 1:
            if ph:
                out += ch
            else:
                out += int(count) * ch
    return out


with open('homeworks5_pack.txt', 'r', encoding='UTF-8') as f:
    test_pack = my_pack(f.read())
with open('homeworks5_unpack.txt', 'w', encoding='UTF-8') as f:
    f.write(my_unpack(test_pack))
