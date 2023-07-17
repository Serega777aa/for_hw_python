# Доработаем задачи 5-6. Создайте класс-фабрику. Класс принимает тип животного
# (название одного из созданных классов) и параметры для этого типа. Внутри класса создайте
# экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings

    def get_info(self):
        return f'для {self.name} размах крыльев {self.wings}'


class Fish(Animal):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'для {self.name} глубина обитания {self.depth}'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def get_info(self):
        return f'для {self.name} вес равен {self.weight}'


class Factory:
    def __init__(self, class_, *args):
        self.class_ = class_
        self.args = args

    def create_instance(self):
        return self.class_(*self.args)


factory_1 = Factory(Mammal, 'cow', 300)
cow = factory_1.create_instance()
print(cow.get_info())

factory_2 = Factory(Fish, 'guppy', 20)
fish = factory_2.create_instance()
print(fish.get_info())


