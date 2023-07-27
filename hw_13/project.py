# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
# Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет есть ли он
# в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа. Если пользователь присутствует
# в списке пользователей проекта, то пользователь, который входит получает его уровень доступа и становится администратором.
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
import json

from hw_13.exceptions import AccessError, LevelError
from hw_13.user import User


class Project:
    def __init__(self, user_lst, admin=None):
        self.admin = admin
        self.user_lst = user_lst

    @classmethod
    def from_json(cls, file_name):
        with(
            open(file_name, 'r', encoding='utf8') as f,
        ):
            dct = json.load(f)
            lst = []
            for l, u in dct.items():
                for u_id, name in u.items():
                    user = User(u_id, name, l)
                    lst.append(user)
            return cls(lst)

    def loggin(self, u_id, name):
        user = User(u_id, name)
        if user not in self.user_lst:
            raise AccessError(name)
        for u in self.user_lst:
            if user == u:
                self.admin = u
                break

    def add_user(self, u_id, name, level):
        if level < self.admin.level:
            raise LevelError(self.admin.name)

        user = User(u_id, name, level)
        self.user_lst.append(user)

    def del_user(self, u_id, name, level):
        if level < self.admin.level:
            raise LevelError(self.admin.name)
        user = User(u_id, name, level)
        self.user_lst.remove(user)

    def __repr__(self):
        return f'Project({self.user_lst}, admin = {self.admin})'

    def __exit__(self, exc_type, exc_value, traceback):
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(self.user_lst, f)


p = Project.from_json('users.json')
print(p)
p.loggin('34', 'igor')
print(p)
p.add_user('324', 'Kolya', '5')
print(p)
p.add_user('349', 'Masha', '1')
print(p)
p.del_user('324', 'Kolya', '5')
print(p)
