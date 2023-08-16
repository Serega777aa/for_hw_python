# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def get_dict(**kwargs):
    res = {}
    for key, value in kwargs.items():
        if not hash(key):
            res[str(value)] = key
        else:
            res[value] = key
    return res


print(get_dict(a=55, b='ttt', c=True))
