# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.
import csv
import pickle


def from_csv_to_pickle_string():
    with open('hw.csv', 'r', newline='') as f:
        reader_lst = list(csv.reader(f))
        lst = []
        keys = [k for k in reader_lst[0]]
        for values in reader_lst[1:]:
            lst.append(dict(zip(keys, values)))
        print(pickle.dumps(lst))


from_csv_to_pickle_string()
