# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv
# файл. Для тестированию возьмите pickle версию файла из предыдущей задачи. Функция должна
# извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import pickle


def from_pickle_to_csv():
    with(
        open('test.pickle', 'rb') as f1,
        open('hw.csv', 'w', newline='') as f2
    ):
        pf = pickle.load(f1)
        writer = csv.DictWriter(f2, fieldnames=pf[0].keys())
        writer.writeheader()
        writer.writerows(pf)


from_pickle_to_csv()
