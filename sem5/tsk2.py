# Дан список интов , повторяющихся элементов в списке нет .
# Нужно преобразовать это множество в строку , сворачивая соседние по числовому ряду числа в диапазоны .
# Примеры : [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11" [1,4,3,2] => "1-4" [1,4] => "1,4"

# lst_int = sorted([1, 4, 5, 2, 3, 9, 8, 11, 0])
# lst_int = sorted([1, 4, 3, 2])
# lst_int = sorted([1, 4])


def border_val(lst_int):
    lst_int = sorted(lst_int)
    ans = [[lst_int[0]]]

    for ind in range(0, len(lst_int) - 1):
        if (ind == len(lst_int) - 2) and (lst_int[ind + 1] == lst_int[ind] + 1):
            ans[-1].append(lst_int[ind + 1])
        if lst_int[ind + 1] != lst_int[ind] + 1:
            ans[-1].append(lst_int[ind])
            ans.append([lst_int[ind + 1]])

    for i in range(len(ans)):
        if max(ans[i]) != min(ans[i]):
            ans[i] = f'{min(ans[i])}-{max(ans[i])}'
        else:
            ans[i] = f'{min(ans[i])}'

    print(', '.join(ans))


border_val([1, 4, 5, 2, 3, 9, 8, 11, 0])
border_val([1, 4, 2, 3])
border_val([1, 4])
