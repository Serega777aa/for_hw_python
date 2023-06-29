# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions


def get_improve(lst):
    if lst[0] < lst[1]:
        temp = lst[0]
    else:
        temp = lst[1]
    for i in range(temp, 1, -1):
        if lst[0] % i == 0 and lst[1] % i == 0:
            lst[0] /= i
            lst[1] /= i
    if lst[0] % lst[1] == 0:
        return str(int(lst[0] / lst[1]))
    return str(int(lst[0])) + '/' + str(int(lst[1]))


num_1 = (input('Дробь 1 = ')).split('/')
num_2 = (input('Дробь 2 = ')).split('/')

prod_frac = fractions.Fraction(int(num_1[0]), int(num_1[1])) * fractions.Fraction(int(num_2[0]), int(num_2[1]))
sum_frac = fractions.Fraction(int(num_1[0]), int(num_1[1])) + fractions.Fraction(int(num_2[0]), int(num_2[1]))

prod_lst = [int(num_1[0]) * int(num_2[0]), int(num_1[1]) * int(num_2[1])]
sum_lst = [int(num_1[0]) * int(num_2[1]) + int(num_2[0]) * int(num_1[1]), int(num_1[1]) * int(num_2[1])]

res_prod = get_improve(prod_lst)
res_sum = get_improve(sum_lst)

print(f'Произведение = {res_prod} Проверка = {prod_frac} {res_prod == str(prod_frac)}')
print(f'Сумма = {res_sum} Проверка = {sum_frac} {res_sum == str(sum_frac)}')
