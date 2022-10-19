# 2. * (вместо задачи
# 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например: >>> num_translate_adv("One") "Один" >>> num_translate_adv("two") "два"

def num_translate(txt):
    dict_value = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'zero': 'ноль'}
    if txt.lower() in dict_value.keys():
        if txt.capitalize() == txt:
            return dict_value[txt.lower()].capitalize()
        return dict_value[txt.lower()]
    else:
        return None

text = input("Enter value: ")
print(f"Answer = {num_translate(text)}")