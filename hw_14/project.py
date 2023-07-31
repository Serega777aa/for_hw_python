import json

from hw_14.exceptions import AccessError, LevelError
from hw_14.user import User


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

    def login(self, u_id, name):
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



