class User:
    def __init__(self, u_id, name, level=None):
        self.level = level
        self.name = name
        self.u_id = u_id

    def __eq__(self, other):
        return self.u_id == other.u_id and self.name == other.name

    def __repr__(self):
        return f'User({self.u_id}, {self.name}, {self.level})'


