import json
from os.path import isfile

id_elem = 0


def get_info():
    person = dict()
    person['surname'] = input('Enter surname of person: ')
    person['name'] = input('Enter name of person: ')
    person['phone'] = input('Enter phone of person: ')
    person['desc'] = input('Enter description of person: ')
    return person


def add_person(person):
    global id_elem
    if isfile('phone_book.js') and id_elem == 0:
        with open('phone_book.js') as book:
            tmp = book.read()
            if len(tmp) > 1:
                tmp = json.loads(tmp)
                id_elem = int(sorted(tmp.keys())[-1]) + 1
    else:
        with open('phone_book.js', 'w') as file:
            pass
    add_id = dict()
    add_id[id_elem] = person
    with open('phone_book.js') as book:
        tmp = book.read()
        if len(tmp) > 1:
            tmp = json.loads(tmp)
        else:
            tmp = dict()
    tmp.update(add_id)
    with open('phone_book.js', 'w') as book:
        json.dump(tmp, book)
    id_elem += 1


def show_contacts():
    if isfile('phone_book.js'):
        with open('phone_book.js') as file:
            tmp = file.read()
            if len(tmp) > 0:
                template = json.loads(tmp)
                print(f'{"surname":^20} | {"name":^20} | {"phone":^12} | {"desc"}')
                for k in template.keys():
                    print(
                        f'{template[k]["surname"]:^20} | {template[k]["name"]:^20} | {template[k]["phone"]:^12} | {template[k]["desc"]}')
            else:
                print('Phone book is empty')
    else:
        print('Phone book is empty')


def find_contact():
    if isfile('phone_book.js'):
        person = get_info()
        with open('phone_book.js') as file:
            tmp = file.read()
            if len(tmp) > 0:
                template = json.loads(tmp)
                print(f'{"surname":^20} | {"name":^20} | {"phone":^12} | {"desc"}')
                for k in template.keys():
                    if ((template[k]['surname'].lower() == person['surname'].lower() or person['surname'] == '') and
                            (template[k]['name'].lower() == person['name'].lower() or person['name'] == '') and
                            (template[k]['phone'] == person['phone'] or person['phone'] == '') and
                            (person['desc'].lower() in template[k]['desc'].lower() or person['desc'] == '')):
                        print(
                            f'{template[k]["surname"]:^20} | {template[k]["name"]:^20} | {template[k]["phone"]:^12} | {template[k]["desc"]}')
            else:
                print('Phone book is empty')
    else:
        print('Phone book is empty')


def import_contacts():
    path = input('Enter path to file:')
    if path.split('.')[-1].lower() == 'csv':
        with open(path, 'r', encoding='utf-8') as impo:
            for row in impo.readlines():
                person = dict()
                data = row.split(';')
                ind = 0
                for key in ("surname", "name", "phone", "desc"):
                    person[key] = data[ind]
                    ind += 1
                add_person(person)
    elif path.split('.')[-1].lower() == 'js':
        with open(path) as impo:
            tmp = json.loads(impo.read())
            for k in tmp.keys():
                add_person(tmp[k])
    else:
        print('Unknown format file')


def export_contact():
    path = input('Where do you want to export the data?: ')
    if path.split('.')[-1].lower() == 'csv':
        with open(path, 'w') as file:
            file.write(f'surname;name;phone;desc\n')
            with open('phone_book.js') as js:
                tmp = json.loads(js.read())
            for k in tmp.keys():
                file.write(f'{tmp[k]["surname"]};{tmp[k]["name"]};{tmp[k]["phone"]};{tmp[k]["desc"]}\n')
    else:
        print('Unknown type file')
