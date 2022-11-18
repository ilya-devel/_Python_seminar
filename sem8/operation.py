import json
import os.path

bd = 'person.js'

def check_bd():
    if not os.path.isfile(bd) or os.path.getsize(bd) < 2:
        with open(bd, 'w') as f:
            tmp = dict()
            json.dump(tmp, f)


def show():
    with open(bd) as file:
        tmp = json.loads(file.read())
    print(f'{"id":^5} | {"surname":^20} | {"name":^20}')
    for key in tmp.keys():
        print(f'{key:^5} | {tmp[key]["surname"]:^20} | {tmp[key]["name"]:^20}')


def add(person):
    with open(bd) as file:
        tmp = json.loads(file.read())
    ind = str(int(sorted(tmp.keys())[-1]) + 1) if len(tmp.keys()) > 0 else '0'
    tmp[ind] = {'surname': person['surname'], 'name': person['name']}
    with open(bd, 'w') as file:
        json.dump(tmp, file)


def search():
    tmp = getinfo()
    tmp['id'] = input('Enter id person: ')
    with open(bd) as file:
        base = json.loads(file.read())
    print(f'{"id":^5} | {"surname":^20} | {"name":^20}')
    for k in base.keys():
        if ((k.lower() == tmp['id'].lower() or tmp['id'] == '') and
                (base[k]['surname'].lower() == tmp['surname'].lower() or tmp['surname'] == '') and
                (base[k]['name'].lower() == tmp['name'].lower() or tmp['name'] == '')):
            print(f'{k:^5} | {base[k]["surname"]:^20} | {base[k]["name"]:^20}')


def getinfo():
    tmp = dict()
    tmp['surname'] = input('Enter surname of person: ')
    tmp['name'] = input('Enter name of person: ')
    return tmp


if __name__ == '__main__':
    pass
