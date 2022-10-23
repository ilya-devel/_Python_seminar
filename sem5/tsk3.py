# Напишите программу, удаляющую из текста все слова, содержащие "абв".

import re

text = '''
фолвадфолва фоовфдаолвф офдавл абвал флвоа фджловф вдалофолафыдвлоафдвола фолдаоф фовладвожоф аофдлва абвл фвабв фдлвоа фждовофа жво оов фдов фвабводфа
'''
mark = r'(\w*абв\w*)'
print(re.findall(mark, text))
for i in list(re.findall(mark, text)):
    print(i)
    text = text.replace(f' {i} ', ' ')

print(text)


text = '''
фолвадфолва фоовфдаолвф офдавл абвал флвоа фджловф вдалофолафыдвлоафдвола фолдаоф
фовладвожоф аофдлва абвл фвабв фдлвоа фждовофа жво оов фдов фвабводфа
'''

lst = text.split()
for i in range(len(lst)):
    if 'абв' in lst[i]:
        lst[i] = ''

print(' '.join(list(filter(lambda x: x != '', lst))))