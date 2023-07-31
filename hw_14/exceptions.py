class BasicException:
    pass


class LevelError(BasicException, Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Админ {self.name} не имеет достаточного уровня'


class AccessError(BasicException, Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} нет в списке доступа'
