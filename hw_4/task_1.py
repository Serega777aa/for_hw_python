# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
# на s (кроме переменной из одной буквы s) на None. Значения не удаляются, а помещаются
# в одноимённые переменные без s на конце.

def change_var():
    lst = list(globals().keys())
    for name in lst:
        if not name.startswith('__'):
            if name.endswith('s') and len(name) > 1:
                globals()[name[:-1]] = globals()[name]
                globals()[name] = None


nums = [55, 66, 77]
number = 567
s = '765'
words = ['привет', 'hello']

change_var()
print(f'{nums=}  {num=} \n{words=}  {word=} \n{s=} \n{number=}')

