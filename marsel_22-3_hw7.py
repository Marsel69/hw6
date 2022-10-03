def binary_search(lst, serch_item):
    low = 0
    n = len(lst) - 1
    serch_res = False
    while low <= n and not serch_res:
        m = (low + n) // 2
        g = lst[m]
        if g == serch_item:
            serch_res = True
            return serch_res

        if g > serch_item:
            n = m - 1
        else:
            low = m + 1
    return serch_res


lst = sorted([23, 43, 9, 65, 87, 95, 54, 34, 6, 10])

value = 43
result = binary_search(lst, value)
print(result)
print(lst)
print(value)

if result:
    print('yes')
else:
    print('Элемент не найден')

def buble_sort(lst):
    for num in range(len(lst) - 1, 0, -1):
        for item in range(num):
            if lst[item] > lst[item + 1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]
    return lst


lst = [10, 4, 8, 9, 6, 5, 2, 3, 7, 1]
print('', lst)
result = buble_sort(lst)
print('Результат сортировки', result)
