# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

ABS_PATH = os.path.abspath('task_1.py')


def get_info_file(abs_path):
    path = abs_path[:abs_path.rfind('\\')].replace('\\', '/')
    name = abs_path[abs_path.rfind('\\') + 1: abs_path.rindex('.')]
    extension = abs_path[abs_path.rfind('.'):]
    return path, name, extension


print(ABS_PATH)
print(get_info_file(ABS_PATH))
