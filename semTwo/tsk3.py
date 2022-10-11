# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if len(text1) > len(text2):
    print(f"Second string meet in first string {text1.count(text2)} time")
elif len(text2) > len(text1):
    print(f"First string meet in second string {text2.count(text1)} time")


count = 0
for i in range(len(text1)):
    if text1[i] == text2[0]:
        if text1[i:i + len(text2)] == text2:
            count += 1

print(count)