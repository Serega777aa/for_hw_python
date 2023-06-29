# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

CHARS_SET = '0123456789abcdef'

num = int(input('целое число = '))
used_hex = hex(num)

res = ''
while num > 0:
    res = CHARS_SET[num % 16] + res
    num //= 16
res = '0x' + res

print(f'{res} == {used_hex}')

