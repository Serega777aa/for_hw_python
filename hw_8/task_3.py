# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные
# директории. Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте
# родительскую директорию. Для каждого объекта укажите файл это или директория. Для файлов сохраните его
# размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорийV.
import csv
import json
import os
import pickle


def get_size_dir(directory):
    size = 0
    for item in os.walk(directory):
        for file in item[2]:
            size += os.path.getsize(os.path.join(item[0], file))
    return size


def traversal_directory(directory):
    lst = []
    for root, dirs, files in os.walk(directory):
        for dir_ in dirs:
            lst.append({
                'obj': dir_,
                'obj_parent': os.path.basename(root),
                'obj_type': 'folder',
                'obj_size': get_size_dir(f'{root}\{dir_}')
            })
        for file in files:
            lst.append({
                'obj': file,
                'obj_parent': os.path.basename(root),
                'obj_type': 'file',
                'obj_size': os.path.getsize(f'{root}\{file}')
            })
        with(
            open('res.json', 'w', encoding='utf8') as f_json,
            open('res.csv', 'w', newline='', encoding='utf8') as f_csv,
            open('res.pickle', 'wb') as f_pickle
        ):
            json.dump(lst, f_json, indent=4)

            writer_csv = csv.DictWriter(f_csv, fieldnames=lst[0].keys())
            writer_csv.writeheader()
            writer_csv.writerows(lst)

            pickle.dump(lst, f_pickle)


traversal_directory(os.getcwd())


