# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите
# 4 успешных расстановки. *Выведите все успешные варианты расстановок

from chess import get_random_pos, check_correct_pos

count_rank = 4

while count_rank:
    pos = get_random_pos()
    if check_correct_pos(pos):
        print(pos)
        count_rank -= 1

