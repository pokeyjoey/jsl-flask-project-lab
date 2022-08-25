class Player:
    attrs = ['id', 'name', 'age', 'height', 'weight', 'shot', 'birth_place', 'birthdate', 'number']

    def __init__(self, player):
        self.__dict__ = dict(zip(attrs, player))
