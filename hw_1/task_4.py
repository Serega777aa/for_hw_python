from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

hidden_num = randint(LOWER_LIMIT, UPPER_LIMIT)
chance = 10
while chance > 0:
    entered_num = int(input(f'Угадайте число за {chance} попыток '))
    if hidden_num > entered_num:
        print('больше')
        chance -= 1
    elif hidden_num < entered_num:
        print('меньше')
        chance -= 1
    else:
        print('Угадали')
        break
if chance == 0:
    print('Вы не угодали')



