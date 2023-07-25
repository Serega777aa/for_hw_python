# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
from time import time


class MyString(str):
    """Класс моя строка"""

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.author = name
        instance.time = time.time()
        return instance

    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __str__(self):
        return f'строка = {self.value} автор = {self.name} время создания = {self.time}'

    def __repr__(self):
        return f'MyString({self.value}, {self.name})'


class Archiv:
    """Класс архив. который хранит пару свойств"""
    instance = None

    def __new__(cls, *args):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.lst = []
        else:
            cls.lst.append(cls.instance.lst.append(args))
        return cls.instance

    def __init__(self, num, str_):
        self.num = num
        self.str_ = str_

    def __str__(self):
        return f'{self.num}, {self.str_}, {self.lst}'

    def __repr__(self):
        return f'Archiv({self.num}, "{self.str_}")'


class Rectangle:
    """Класс прямоугольник"""

    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b else a

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b

    def __add__(self, other):
        new_p = self.perimeter() + other.perimeter()
        new_a = self.a + self.b
        new_b = new_p / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        new_p = abs(self.perimeter() - other.perimeter())
        new_a = abs(self.a - self.b)
        new_b = new_p / 2 - new_a
        return Rectangle(new_a, new_b)

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.area() >= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.a}, {self.b}'

    def __repr__(self):
        return f'Rectangle({self.a}, {self.b})'
