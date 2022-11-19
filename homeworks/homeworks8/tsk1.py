# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(strnum: str):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if strnum in num_dict.keys():
        return num_dict[strnum]
    else:
        return None


print(num_translate("one"))
print(num_translate("eight"))
print()


# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
def num_translate_adv(strnum: str):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if strnum.lower() in num_dict.keys():
        if strnum == strnum.capitalize():
            return num_dict[strnum.lower()].capitalize()
        else:
            return num_dict[strnum]
    else:
        return None


print(num_translate_adv("One"))
print(num_translate_adv("eight"))
print()


# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*args):
    dict_name = dict()
    for name in args:
        if name.strip().capitalize()[0] in dict_name.keys():
            dict_name[name.strip().capitalize()[0]].append(name.strip().capitalize())
        else:
            dict_name[name.strip().capitalize()[0]] = [name.strip().capitalize()]
    return dict_name


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
num_d = thesaurus("Иван", "Мария", "Петр", "Илья")
for key in sorted(num_d.keys()):
    print(f'{key}: {", ".join(sorted(num_d[key]))}')
print()


# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?
def thesaurus_adv(*args):
    dict_name = dict()
    for name in args:
        tmp = name.strip().split()
        if tmp[1].capitalize()[0] in dict_name.keys():
            if tmp[0].capitalize()[0] in dict_name[tmp[1].capitalize()[0]].keys():
                dict_name[tmp[1].capitalize()[0]][tmp[0].capitalize()[0]].append(name)
            else:
                dict_name[tmp[1].capitalize()[0]][tmp[0].capitalize()[0]] = [name]
        else:
            dict_name[tmp[1].capitalize()[0]] = dict()
            dict_name[tmp[1].capitalize()[0]][tmp[0].capitalize()[0]] = [name]
    return dict_name


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
num_d = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
for sur in sorted(num_d.keys()):
    print(f'{sur}:')
    for name in sorted(num_d[sur].keys()):
        print(f'\t{name}: {", ".join(sorted(num_d[sur][name]))}')
