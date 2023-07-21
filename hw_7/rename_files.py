# — Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
import os


def rename_files(new_name, ext, new_ext):
    print(os.getcwd())
    temp = [file for file in os.listdir() if os.path.isfile(file) and file.rsplit(".", 1)[1] == ext]
    for num, file in enumerate(temp, 1):
        os.rename(file, f'{str(file.rsplit(".", 1)[0])}_{new_name}_{num}.{new_ext}')


rename_files('new_name', 'txt', 'doc')

