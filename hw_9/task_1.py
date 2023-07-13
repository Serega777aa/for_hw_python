# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
import math
from random import randint


def deco2(func):
    lst = []
    def wrapper(*args):
        lst.append({f'{args}': func(*args)})
        with open('hw_9.json', 'w', encoding='utf8') as f:
            json.dump(lst, f, indent=2)

    return wrapper


def deco1(func):
    def wrapper(*args):
        with open('hw_9.csv', 'r', newline='', encoding='utf8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                func(*map(int, row))

    return wrapper


def gen_csv_file():
    lst = [[randint(1, 10) for _ in range(3)] for _ in range(100, 1000)]
    with open('hw_9.csv', 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(lst)

@deco1
@deco2
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        return 'not roots!'


gen_csv_file()

find_roots(8, 8, 2)


