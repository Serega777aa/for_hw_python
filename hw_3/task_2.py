#  Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
#  В результирующем списке не должно быть дубликатов.

lst = [1, 2, 3, 4, 5, 1, 3, 7, 6, 4, 7]
dublicate_lst = []

for num in lst:
    if lst.count(num) > 1:
        if num not in dublicate_lst:
            dublicate_lst.append(num)
print(f'{lst = } \n{dublicate_lst = }')
