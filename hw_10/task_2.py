# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.
import csv
import pickle


class Serialization:
    def __init__(self, pickle_file):
        self.pickle_file = pickle_file

    def from_pickle_to_csv(self):
        with(
            open(self.pickle_file, 'rb') as f1,
            open('file.csv', 'w', newline='', encoding='utf8') as f2
        ):
            pf = pickle.load(f1)
            writer = csv.DictWriter(f2, fieldnames=pf[0].keys())
            writer.writeheader()
            writer.writerows(pf)


ser = Serialization('file.pickle')
ser.from_pickle_to_csv()


