# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends = {'Миша': ('спички', 'нож', 'палатка', 'продукты'),
           'Леша': ('компас', 'топор', 'дождевик', 'вода'),
           'Саша': ('котелок', 'спички', 'кружка', 'продукты')}

all_things = set()
uniq_things = {}
except_things = {}

for friend in friends:
    all_things |= set(friends[friend])
    uniq_obj = set(friends[friend])
    except_obj = set()
    for next_friend in friends:
        if next_friend != friend:
            uniq_obj -= set(friends[next_friend])
            if except_obj:
                except_obj.intersection_update(set(friends[next_friend]))
            else:
                except_obj |= (set(friends[next_friend]))

    uniq_things[friend] = uniq_obj
    except_things[friend] = except_obj - set(friends[friend])

print(f'Вещи, которые взяли все три друга: {all_things}\n\
Уникальные вещи: {uniq_things} \nВещи, которые есть у всех друзей кроме одного: {except_things}')