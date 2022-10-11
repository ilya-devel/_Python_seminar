# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. *Пример:* - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

value = int(input("Enter N value: "))
dict_val = {i: (3 * i + 1) for i in range(1, value + 1)}
print(dict_val)
print(', '.join([f"{k}: {v}" for k, v in dict_val.items()]))