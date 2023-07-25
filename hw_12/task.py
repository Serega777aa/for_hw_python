# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError("Invalid name format")


class Student:
    name = NameValidator()
    surname = NameValidator()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.subject = self.get_subjects()
        self._scores = {self.subject[0]: [], self.subject[1]: [], self.subject[2]: []}
        self._results = {self.subject[0]: [], self.subject[1]: [], self.subject[2]: []}

    @staticmethod
    def get_subjects():
        with open('subjects.csv', 'r', encoding='utf8') as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    def set_score(self, subject, score):
        if score < 2 or score > 5:
            raise ValueError("Invalid score")
        self._scores[subject].append(score)

    def set_result(self, subject, result):
        if result < 0 or result > 100:
            raise ValueError("Invalid result")
        self._results[subject].append(result)

    def get_average_score(self, subject):
        if not self._scores:
            return 0
        return sum(self._scores[subject]) / len(self._scores[subject])

    def get_average_result(self, subject):
        if not self._results:
            return 0
        return sum(self._results[subject]) / len(self._results[subject])


student = Student('Иван', 'Иванов')
student_2 = Student('Александрова', 'Александра')

student.set_score('математика', 4)
student.set_score('математика', 5)
student.set_result('математика', 85)
student.set_result('математика', 95)
student_2.set_score('физика', 4)
student_2.set_score('физика', 3)

print(student.get_average_score('математика'))
print(student.get_average_result('математика'))
print(student_2.get_average_score('физика'))
